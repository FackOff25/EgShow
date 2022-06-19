from django.shortcuts import render

# Create your views here.

IMAGES = range(12)


def loaded_images(request):
    return render(request, "images.html", {'images': IMAGES})


def build_new(request):
    return render(request, "upload.html")


def image(request):
    return render(request, "image.html")

