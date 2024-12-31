from rest_framework.serializers import ModelSerializer
from api.models import AutorModel

class AutorSerializer(ModelSerializer):
    class Meta:
        model = AutorModel
        fields = ['id','nombres','apellidos','email']