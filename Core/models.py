from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(null=True, blank= True)

    def __str__(self):
        return f'{self.name}'
        
class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    header = models.CharField(max_length=256)
    text = models.TextField()
    image = models.ImageField( null = True, blank = True)
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    read_count = models.PositiveIntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.header} {self.read_count}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='comments',on_delete=models.CASCADE)
    text = models.TextField()
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} {self.blog}'
