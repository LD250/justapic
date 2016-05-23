from django.contrib.auth.models import User
from rest_framework import serializers

from album.models import UserAlbum


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')


class UserAlbumSerializer(serializers.ModelSerializer):
    #album = UserAlbumSerializer(read_only=True)
    class Meta:
        model = UserAlbum
        fields = ('id', 'user', 'photo')

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAlbum
        fields = ('id', 'photo')


class AlbumByUserSerializer(serializers.ModelSerializer):
    useralbum = AlbumSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'useralbum')
