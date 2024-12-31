from rest_framework.serializers import ModelSerializer
from api.models import SubcategoriaModel

class SubcategoriaSerializer(ModelSerializer):
    class Meta:
        model = SubcategoriaModel
        fields = ['id','nombre','descripcion']