from rest_framework.serializers import ModelSerializer
from api.models import CategoriaModel

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = CategoriaModel
        fields = ['id','nombre','descripcion']