from rest_framework import serializers
from users.models import User, Category, Country

#
# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=255)
#     email = serializers.CharField(max_length=255)
#     categories = serializers.SlugRelatedField(
#         many=True,
#         queryset=Category.objects.all(),
#         slug_field='name')
#     countries = serializers.SlugRelatedField(
#         many=True,
#         queryset=Country.objects.all(),
#         slug_field='name')


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
        extra_kwargs = {
        'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.categories.set(validated_data['categories'])
        instance.countries.set(validated_data['countries'])
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            elif attr == 'categories':
                instance.categories.set(validated_data[attr])
            elif attr == 'countries':
                instance.countries.set(validated_data[attr])
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class CountryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']
