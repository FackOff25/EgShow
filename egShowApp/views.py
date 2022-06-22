import sys
from threading import Thread

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

from egShowApp.models import TiledImage
from django.views.decorators.http import require_http_methods
from egShowApp.forms import TiledImageForm


def paginate(objects_list, request, per_page=5):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page')
    iterators = paginator.get_page(page)
    return iterators


def new_images(request):
    iterators = paginate(TiledImage.objects.get_last(), request, 15)
    return render(request, "images.html", {'iterators': iterators})


def alph_images(request):
    iterators = paginate(TiledImage.objects.get_in_alph(), request, 15)
    return render(request, "images.html", {'iterators': iterators})


@require_http_methods(['POST', 'GET'])
def build_new(request):
    if request.method == 'POST':

        def save_form(form_to_save):
            if form_to_save.is_valid():
                form_to_save.save()
            else:
                print("Form invalid", file=sys.stderr)

        form = TiledImageForm(data=request.POST, files=request.FILES)
        pr = Thread(target=save_form, args=(form, ))
        pr.start()
        # second of wait to check form validation and avoid sharing memory
        pr.join(0.5)
        return redirect(reverse('New images'))

    form = TiledImageForm()
    return render(request, "upload.html", {'form': form})


def image(request, iid: int):

    try:
        the_image = TiledImage.objects.get(pk=iid)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    return render(request, "image.html", {'image': the_image})
