from django.db import models

class CategoriaModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    descripcion = models.CharField(max_length=128)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        app_label = 'api'
        db_table = 'tbl_categorias'
        db_table_comment = 'Tabla que contiene todas las categorias en las que se pueden agrupar los posts.'