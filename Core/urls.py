from django.urls import path
from .views import HomePageView, BlogDetailView, AddBlogView

urlpatterns = [
    path('', HomePageView.as_view(),  name = 'home'),
    path('blog/<int:pk>', BlogDetailView.as_view(),  name = 'detail'),
    path('add-blog', AddBlogView.as_view(),  name = 'add-blog')
]
