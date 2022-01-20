from importlib.util import module_for_loader
from modulefinder import Module
from time import timezone
from django.utils import timezone
from venv import create
from xml.parsers.expat import model
from django.db import models
from pkg_resources import EGG_DIST

# Create your models here.
class PrimerTabla(models.Model):
    nombre = models.CharField( max_length=50, null=False)
    edad = models.IntegerField(default=0, null=False)
    created = models.DateTimeField(default=timezone.now)
    edit= models.DateTimeField(blank=True, null=True, default=None)
