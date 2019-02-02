from django.urls import path
from . import views


urlpatterns = [
    path('index', views.IndexPageView.as_view(), name='index'),
    # path('json', views.json_response, name='json_response')
    ]
