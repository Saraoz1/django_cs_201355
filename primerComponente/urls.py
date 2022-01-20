from django.urls import path,re_path
from django.conf.urls import include

from primerComponente.views import PrimerTablalist

urlpatterns = [ 
    re_path(r'^primer_componente/$',PrimerTablalist.as_view()),

]
