from django.contrib.auth.models import User
from rest_framework import viewsets

from album.models import UserAlbum
from album.serializers import UserAlbumSerializer, UserSerializer, AlbumByUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserAlbumViewSet(viewsets.ModelViewSet):
    queryset = UserAlbum.objects.all()
    serializer_class = UserAlbumSerializer


class AlbumByUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().prefetch_related('useralbum')
    serializer_class = AlbumByUserSerializer
