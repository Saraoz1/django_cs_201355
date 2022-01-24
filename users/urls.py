from django.urls import path,re_path
from django.conf.urls import include

from users.views import PrimerTablalistUser

urlpatterns = [ 
    re_path(r'^registro/$',PrimerTablalistUser.as_view()),

]