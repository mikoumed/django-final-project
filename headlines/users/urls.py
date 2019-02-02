from django.contrib.auth.views import LoginView
from django.urls import path
from . import views






urlpatterns = [
    path('signup/', views.SignUp.as_view(redirect_authenticated_user=True), name='signup'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    ]
