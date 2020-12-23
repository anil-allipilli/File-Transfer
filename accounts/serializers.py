from rest_framework import serializers
from accounts.models import MyUser as User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(max_length=12, required=True)
    company_name = serializers.CharField(max_length=150, required=True)
    company_logo = serializers.ImageField(required=True)

    class Meta:
        model = User
        fields = [
            "password",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "company_name",
            "company_logo",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    # def create(self, validated_data):
    #     user = super().create(validated_data)
    #     user.set_password(validated_data["password"])
    #     user.save()
    #     return user

    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     user = super().update(instance, validated_data)
    #     try:
    #         user.set_password(validated_data["password"])
    #         user.save()
    #     except KeyError:
    #         pass
    #     return user