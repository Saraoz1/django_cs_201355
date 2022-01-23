from urllib import response
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView


#importaciones de modelos agregados
from primerComponente.models import PrimerTabla

#improtaciones de serializadores
from primerComponente.serializers import PrimerTablaSerializers

# Create your views here.
class PrimerTablalist(APIView):
    def get (self, request, format=None):
        queryset=PrimerTabla.objects.all()
        serializer=PrimerTablaSerializers(queryset,many=True,context={'request':request})
        return Response(serializer.data)
 