from django.db import models

class AutorModel(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    email = models.EmailField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.apellidos} {self.nombres}'
    
    class Meta:
        app_label = 'api'
        db_table = 'tbl_autores'
        db_table_comment = 'Tabla que contiene todos los autores que pueden crear posts.'
