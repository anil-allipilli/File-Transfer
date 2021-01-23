from rest_framework import viewsets
from products.models import Product, ProductFile
from products.serializers import ProductSerializer, ProductFileSerializer
from products.permissions import IsItSharedWithUser


class ProductViewset(viewsets.ModelViewSet):
    permission_classes = [IsItSharedWithUser]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductFileViewset(viewsets.ModelViewSet):

    queryset = ProductFile.objects.all()
    serializer_class = ProductFileSerializer


class MyProductsViewset(viewsets.ModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        the_user = self.request.user
        return the_user.my_products.all()


class SharedProductsViewset(viewsets.ModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        the_user = self.request.user
        return the_user.shared_products.all()