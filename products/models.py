from django.db import models
import os
from accounts.models import MyUser


class Product(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name="my_products"
    )
    product_users = models.ManyToManyField(MyUser, related_name="shared_products")

    def __str__(self):
        return self.name


class ProductFile(models.Model):
    file = models.FileField(upload_to="files/")
    product = models.ForeignKey(
        Product, related_name="product_files", on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.product.name