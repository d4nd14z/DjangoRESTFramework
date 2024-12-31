from django.db import models
from api.models import AutorModel, CategoriaModel, SubcategoriaModel

class PostModel(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=128)
    contenido = models.TextField()
    autor = models.ForeignKey('AutorModel', on_delete=models.CASCADE)
    categoria = models.ForeignKey('CategoriaModel', on_delete=models.CASCADE)
    subcategoria = models.ForeignKey('SubcategoriaModel', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        app_label = 'api'
        db_table = 'tbl_posts'
        db_table_comment = 'Tabla que contiene todas las entradas que han sido creadas del blog'
