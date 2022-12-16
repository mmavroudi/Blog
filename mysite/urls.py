"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

import projects
import projects.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', projects.views.home, name='home'),
    path('posts', projects.views.post_detail_view, name='post_detail_view'),
    path('random-post', projects.views.random_post, name='random_post'),
    path('single-post/<slug:slug>', projects.views.single_post_view, name='single_post'),
    path('category/<slug:category_slug>', projects.views.category_view, name='category'),
    path('about/', TemplateView.as_view(template_name='about.html'))
   #path('about', projects.views.about_view, name='about')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
