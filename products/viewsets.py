from rest_framework import viewsets
from products.models import Product, ProductFile
from products.serializers import ProductSerializer, ProductFileSerializer


class ProductViewset(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductFileViewset(viewsets.ModelViewSet):

    queryset = ProductFile.objects.all()
    serializer_class = ProductFileSerializer
