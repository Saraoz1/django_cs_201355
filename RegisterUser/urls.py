from django.urls import path, re_path
from django.conf.urls import include

#portacion de vistas
from RegisterUser.views import RegisterAPI


urlpatterns= [
    re_path(r'^user/$', RegisterAPI.as_view()),
]