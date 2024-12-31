from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from api.serializers import PostSerializer
from api.models import PostModel, CategoriaModel, SubcategoriaModel

class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = PostModel.objects.all()

    # /api/posts/categoria/?categoryId=1
    @action(detail=False, methods=['get'], url_path='categoria')
    def obtenerPostsPorCategoria(self, request):        
        categoryId = request.query_params.get('categoryId', None) #Recibir parametro por la URL
        if categoryId is not None:             
            try: #Validar que la categoria sea una categoria valida !!!             
                categoria = CategoriaModel.objects.get(id=categoryId) #Obtener la categoria
                posts = PostModel.objects.filter(categoria=categoryId)
                serializer = PostSerializer(posts, many=True)
                return Response(serializer.data, status=200)
            except CategoriaModel.DoesNotExist: #Si no se encontro la categoria
                return Response({'status': 404, 'error': 'Categoria No Encontrada'}, status=404) #Respondo con el mensaje de error            
        else: 
            return Response({'status': 400, 'error': 'Categoria No Especificada'}, status=400)
        
    # /api/posts/subcategoria/?subcategoryId=1
    @action(detail=False, methods=['get'], url_path='subcategoria')
    def obtenerPostsBySubcategoria(self, request):
        subcategoryId = request.query_params.get('subcategoryId', None) #Recibir parametro por la URL
        if subcategoryId is not None:
            try: 
                subcategoria = SubcategoriaModel.objects.get(id=subcategoryId)
                posts = PostModel.objects.filter(subcategoria=subcategoryId)
                serializer = PostSerializer(posts, many=True)
                return Response(serializer.data, status=200)
            except SubcategoriaModel.DoesNotExist: 
                return Response({'status': 404, 'error': 'Subcategoria No Encontrada'}, status=404)
        else: 
            return Response({'status': 400, 'error': 'Subcategoria No Especificada'}, status=400)
        
    # /api/posts/categandsub/?categoryId=1&subcategoryId=1
    @action(detail=False, methods=['get'], url_path='categandsub')
    def obtenerPostsByCategoriaAndSubcategoria(self, request):
        categoryId = request.query_params.get('categoryId', None)
        subcategoryId = request.query_params.get('subcategoryId', None)
        if categoryId is not None and subcategoryId is not None: 
            try: 
                categoria = CategoriaModel.objects.get(id=categoryId)
                subcategoria = SubcategoriaModel.objects.get(id=subcategoryId)
                posts = PostModel.objects.filter(categoria=categoryId, subcategoria=subcategoryId)
                serializer = PostSerializer(posts, many=True)
                return Response(serializer.data, status=200)
            except CategoriaModel.DoesNotExist: 
                return Response({'status': 404, 'error': 'Categoria No Encontrada'}, status=404)
            except SubcategoriaModel.DoesNotExist:
                return Response({'status': 404, 'error': 'Subcategoria No Encontrada'}, status=404)
        else:
            return Response({'status': 400, 'error': 'Categoria y/o Subcategoria No Especificada'}, status=400)

