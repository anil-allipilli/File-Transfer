from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins
from products.models import Product, ProductFile
from accounts.models import MyUser
from products.serializers import ProductSerializer


@api_view(["POST"])
def create_product(request):

    for key, value in request.data.items():
        if "productName" in key:
            print(key, value)
            new_product = Product(name=value, owner=request.user)

        if "users" in key:
            print(key, value)
            sharing_user = MyUser.objects.get(email=value)
            new_product.product_users.add(sharing_user)
        new_product.save()

        if "file" in key:
            print(key, value)
            new_product_file = ProductFile(file=value, product=new_product)
            new_product_file.save()

    return Response(ProductSerializer(new_product, context={"request": request}).data)
