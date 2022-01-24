from django.urls import path,re_path
from django.conf.urls import include

from registroUsuarios.views import PrimerTablalistUser

urlpatterns = [ 
    re_path(r'^listaUser/$',PrimerTablalistUser.as_view()),

]
