from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

# router.register('create', views.UserCreate, base_name='create_user')
router.register('users', views.UserModelViewSet, base_name='users')
router.register('categories', views.CategoryModelViewSet, base_name='categories')
router.register('countries', views.CountryModelViewset, base_name='countries')

urlpatterns = [
    # path('list/', views.UserList.as_view(), name='users_list'),
    # path('json', views.json_response, name='json_response')
    ]

urlpatterns += router.urls
