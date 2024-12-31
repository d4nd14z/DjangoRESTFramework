from django.contrib import admin
from api.models import AutorModel, CategoriaModel, SubcategoriaModel, PostModel

# Register your models here.
@admin.register(AutorModel)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['id','nombres','apellidos','email','status','created_at']

@admin.register(CategoriaModel)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion','status','created_at']

@admin.register(SubcategoriaModel)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion','categoria','status','created_at']

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','titulo','autor','categoria','subcategoria','status','created_at']