"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from server.views import Login, Usuario
import views

urlpatterns = [
    url(r'^$', Login.as_view(), name='login'),
    url(r'^usuario/', Usuario.as_view(), name='getpid'),
    url(r'^salir/', views.salir, name='salir'),
    url(r'^comprar/', views.comprar, name='comprar'),
    url(r'^tarjeta/', views.tarjeta, name='tarjeta'),
    url(r'^programa/', views.programa, name='tarjeta'),
]
