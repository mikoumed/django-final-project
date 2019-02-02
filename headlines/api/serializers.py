from rest_framework import serializers
from users.models import User, Category, Country


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    categories = serializers.SlugRelatedField(
        many=True,
        queryset=Category.objects.all(),
        slug_field='name')
    countries = serializers.SlugRelatedField(
        many=True,
        queryset=Country.objects.all(),
        slug_field='name')


class UserModelSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True,
        queryset=Category.objects.all(),
        slug_field='name')
    countries = serializers.SlugRelatedField(
        many=True,
        queryset=Country.objects.all(),
        slug_field='name')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'categories', 'countries']
