from django.db import models
from api.models.CategoriaModel import CategoriaModel

class SubcategoriaModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=128)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        app_label = 'api'
        db_table = 'tbl_subcategorias'
        db_table_comment = 'Tabla que contiene todas las subcategorias en las que se pueden agrupar los posts.'