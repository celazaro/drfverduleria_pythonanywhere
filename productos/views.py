from rest_framework import viewsets


from .models import Categoria, Productos 
from .serializers import CategoriaSerializers, ProductoSerializers 

class CategoriaViewSet (viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

class ProductoViewSet (viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializers
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Filtrado por Categoría
        categoria = self.request.query_params.get('categoria')
        if categoria:
            queryset = queryset.filter(categoria = categoria)
        
        # Filtrado por nombre de producto
        search = self.request.query_params.get('search', None)
        if search is not None:
            queryset = queryset.filter(nombre__icontains = search) | queryset.filter(descripcion__icontains = search )
        
        return queryset

    
    