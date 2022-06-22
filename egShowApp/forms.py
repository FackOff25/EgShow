import os
import subprocess

from django import forms
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from egShowApp.models import TiledImage
from egShow.settings import MEDIA_ROOT, MEDIA_URL


class TiledImageForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'placeholder': 'Your image will have this name',
                                                                       'class': 'form-control'}))
    image = forms.ImageField(label='Upload image', widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = TiledImage
        fields = ['name', 'image']

    def save(self, *args, **kwargs):
        self.instance = TiledImage.objects.create(name=self.cleaned_data['name'])
        directory = str(MEDIA_ROOT) + "/tiled/" + str(self.instance.pk)
        original_umask = os.umask(000)
        os.makedirs(directory, 0o777)
        os.umask(original_umask)
        path = default_storage.save('tmp/temp.jpg', ContentFile(self.cleaned_data['image'].read()))
        exit_code = subprocess.check_call(['back/tiler/tiler.o', str(self.instance.pk),
                                           self.instance.name, "media/" + path, 'media/tiled/'])
        os.remove(str(MEDIA_ROOT) + "/" + path)
        self.instance.directory = MEDIA_URL + "tiled/" + str(self.instance.pk)
        self.instance.save()
