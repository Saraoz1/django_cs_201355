from urllib import response
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView


#importaciones de modelos agregados
from users.models import PrimerTablaUser

#improtaciones de serializadores
from users.serializers import PrimerTablaSerializers

# Create your views here.
class PrimerTablalistUser(APIView):
    def get (self, request, format=None):
        queryset=PrimerTablaUser.objects.all()
        serializer=PrimerTablaSerializers(queryset,many=True,context={'request':request})
        return Response(serializer.data)
 