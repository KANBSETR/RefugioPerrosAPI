"""
URL configuration for refugio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from refugioPerro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('refugio/', views.listar_perros, name='refugio'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('signin/', views.inicioSesion, name='signin'),
    path('agregar/', views.agregarPerro, name='AgregarPerro'),
    path('refugio/<int:perro_id>/', views.perro_detail, name='perro_detail'),
    path('refugio/<int:perro_id>/delete', views.perro_delete, name='perro_delete'),
    
]
