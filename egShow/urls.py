"""egShow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from egShowApp import views
from egShow import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.new_images, name="Main"),
                  path('new/', views.new_images, name="New images"),
                  path('alph/', views.alph_images, name="Alphabet images"),
                  path('upload/', views.build_new, name="Build new pyramid"),
                  path('image/<int:iid>/', views.image, name="Show image"),
              ] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0]) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
