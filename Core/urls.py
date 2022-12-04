from django.urls import path
from .views import HomePageView, BlogDetailView, AddBlogView, BlogLike
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomePageView.as_view(),  name = 'home'),
    path('blog/<int:pk>', BlogDetailView.as_view(),  name = 'detail'),
    path('like/<int:pk>', BlogLike,  name = 'blog_like'),
    path('add-blog', login_required(AddBlogView.as_view()),  name = 'add-blog'),
]
