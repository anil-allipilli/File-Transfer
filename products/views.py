from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, mixins
from products.models import Product, ProductFile
from accounts.models import MyUser
from products.serializers import ProductSerializer
from products.tasks import send_product_email_to_users


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
        users_list = [x.email for x in new_product.product_users.all()]

        send_product_email_to_users.delay(
            new_product.name, new_product.owner.email, users_list
        )
        if "file" in key:
            print(key, value)
            new_product_file = ProductFile(file=value, product=new_product)
            new_product_file.save()

    return Response(ProductSerializer(new_product, context={"request": request}).data)
