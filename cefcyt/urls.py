"""cefcyt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from paginace import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admincemk', admin.site.urls),
    path('', views.raiz),
    path ('about', views.about),
    path ('blog', views.blog),
    path ('blog/<slug:pk>', views.single_blog, name='single_blog'),
    path('course', views.course),
    path('shop', views.shop),
    path('eventos', views.eventos),
    path('contact', views.contact),
    path('inicio/', views.index),
    path('correo', views.crear_correo, name='crear_correo'),
    path('contacto', views.crear_contacto, name='crear_contacto'),
    path('data_inicial', views.data_inicial, name='data_inicial'),
    path('busqueda',views.busqueda),
    path('tag1', views.tag1),
    path('tag2', views.tag2),
    path('tag3', views.tag3),
    path('tag4', views.tag4),
    path('tag5', views.tag5),
    path('tag6', views.tag6),
    path('tag7', views.tag7),
    path('tag8', views.tag8),
    path('tag9', views.tag9),
    path('tag10', views.tag10),
    path('tag11', views.tag11),
    path('tag12', views.tag12),
    path("search", views.search),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
