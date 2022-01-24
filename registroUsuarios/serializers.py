from dataclasses import field
from rest_framework  import routers,serializers, viewsets 

#importacion de modelos 
from registroUsuarios.models import PrimerTablaUser

class PrimerTablaSerializers(serializers.ModelSerializer):
    class Meta:
        model = PrimerTablaUser
        fields = ('usuario', 'contrasena', 'correo')