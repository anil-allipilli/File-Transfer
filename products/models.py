from django.db import models
import os
from accounts.models import MyUser


class ProductFile(models.Model):
    file = models.FileField(upload_to="files/")
    product = models.ForeignKey("Product", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.file()


class Product(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="owner")
    product_users = models.ManyToManyField(MyUser, related_name="users")

    def __str__(self):
        return self.name
