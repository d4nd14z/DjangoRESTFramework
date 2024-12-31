from rest_framework.serializers import ModelSerializer
from api.serializers.AutorSerializer import AutorSerializer
from api.serializers.CategoriaSerializer import CategoriaSerializer
from api.serializers.SubcategoriaSerializer import SubcategoriaSerializer
from api.models import PostModel

class PostSerializer(ModelSerializer):

    autor = AutorSerializer(read_only=True)
    categoria = CategoriaSerializer(read_only=True)
    subcategoria = SubcategoriaSerializer(read_only=True)

    class Meta:
        model = PostModel
        fields = ['id','titulo', 'contenido', 'autor', 'categoria', 'subcategoria', 'status', 'created_at'] #Serializar todos los campos del objeto PostModel