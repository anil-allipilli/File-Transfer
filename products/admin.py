from django.contrib import admin

from products.models import Product, ProductFile

admin.site.register(Product)
admin.site.register(ProductFile)
