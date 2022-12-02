from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='user-images', default='/admin-photo1.jpg')

    def __str__(self):
        return f'{self.user}'