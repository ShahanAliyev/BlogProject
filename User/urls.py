
from django.urls import path, include
from .views import UserRegisterView, UserLoginView, ContactUsView, AboutUsView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register', UserRegisterView.as_view(), name = 'register'),
    path('login', UserLoginView.as_view(), name = 'login'),
    path('logout', LogoutView.as_view(), name = 'logout'),
    path('contact_us', ContactUsView.as_view(), name = 'contact_us'),
    path('about_us', AboutUsView.as_view(), name = 'about_us'),
]