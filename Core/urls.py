from django.urls import path
from .views import HomePageView, BlogDetailView, AddBlogView, BlogLike

urlpatterns = [
    path('', HomePageView.as_view(),  name = 'home'),
    path('blog/<int:pk>', BlogDetailView.as_view(),  name = 'detail'),
    path('like/<int:pk>', BlogLike,  name = 'blog_like'),
    path('add-blog', AddBlogView.as_view(),  name = 'add-blog'),
]
