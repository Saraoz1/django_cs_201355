from dataclasses import field
from rest_framework  import routers,serializers, viewsets 

#importacion de modelos 
from primerComponente.models import PrimerTabla

class PrimerTablaSerializers(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        fields = ('nombre', 'edad')