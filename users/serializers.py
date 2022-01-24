from dataclasses import field
from rest_framework  import routers,serializers, viewsets 


#importacion de modelos 
from users.models import PrimerTablaUser

class PrimerTablaSerializers(serializers.ModelSerializer):
    class Meta:
        model = PrimerTablaUser
        fields = ('contrasena', 'usuario','correo')