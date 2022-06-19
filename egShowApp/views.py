from django.shortcuts import render

# Create your views here.


def loaded_images(request):
    return render(request, "images.html")


def build_new(request):
    return render(request, "upload.html")


def image(request):
    return render(request, "image.html")

