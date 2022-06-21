from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render
from egShowApp.models import TiledImage

# Create your views here.

IMAGES = range(12)


def paginate(objects_list, request, per_page=5):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page')
    iterators = paginator.get_page(page)
    return iterators


def new_images(request):
    iterators = paginate(TiledImage.objects.get_last(), request, 5)
    return render(request, "images.html", {'iterators': iterators})


def alph_images(request):
    iterators = paginate(TiledImage.objects.get_in_alph(), request, 5)
    return render(request, "images.html", {'iterators': iterators})


def build_new(request):
    return render(request, "upload.html")


def image(request, iid: int):
    try:
        the_image = TiledImage.objects.get(pk=iid)
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    return render(request, "image.html", {'image': the_image})
