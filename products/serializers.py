from rest_framework import serializers

from products.models import Product, ProductFile


class ProductFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFile
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    product_files = ProductFileSerializer(many=True, read_only=True)
    product_users = serializers.StringRelatedField(many=True)
    owner = serializers.StringRelatedField(many=False)

    class Meta:
        model = Product
        fields = ["id", "name", "owner", "product_users", "product_files"]
