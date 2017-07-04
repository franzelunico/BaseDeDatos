from django.conf.urls import url
from django.contrib import admin
from server.views import Login, UserView, salir, programa, comprar, tarjeta
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', Login.as_view(), name='login'),
    url(r'^usuario/', login_required(UserView.as_view())),
    url(r'^admin/', admin.site.urls),
    url(r'^salir/', salir, name='salir'),
    url(r'^programa/', programa, name='programa'),
    url(r'^comprar/', comprar, name='comprar'),
    url(r'^tarjeta/', tarjeta, name='tarjeta'),
]
