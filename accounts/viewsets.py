from rest_framework import viewsets
from accounts.models import MyUser
from accounts.serializers import UserSerializer


class MyUserViewSet(viewsets.ModelViewSet):

    queryset = MyUser.objects.all()
    serializer_class = UserSerializer