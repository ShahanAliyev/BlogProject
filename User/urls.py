
from django.urls import path, include
from .views import UserRegisterView, UserLoginView, AboutUsView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register', UserRegisterView.as_view(), name = 'register'),
    path('login', UserLoginView.as_view(), name = 'login'),
    path('logout', LogoutView.as_view(), name = 'logout'),
    path('about_us', AboutUsView.as_view(), name = 'about_us'),
]