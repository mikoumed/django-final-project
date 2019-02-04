from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, UserModelSerializer
from users.models import User, Category, Country
from rest_framework import viewsets, mixins
from rest_framework.viewsets import GenericViewSet




# class UserList(APIView):
#     def get(self, request):
#         qs = User.objects.all()
#         serializer = UserSerializer(qs, many=True)
#         return Response(serializer.data)
#
# class UserCreate(viewsets.ViewSet):
#     def create(self, request):
#         serializer = UserModelSerializer(data=request.data)
#         if serializer.is_valid():
#             categories = serializer.validated_data.pop('categories')
#             countries = serializer.validated_data.pop('countries')
#             user = User.objects.create_user(**serializer.validated_data)
#             user.categories.set(categories)
#             user.countries.set(countries)
#
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserModelViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet):

    serializer_class = UserModelSerializer
    queryset = User.objects.all()
