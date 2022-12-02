from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='user-images', default='/admin-photo1.jpg')
    bio = models.TextField(null=True, blank=True)
    work_status = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'

class Social(models.Model):
    custom_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name="socials")
    name = models.CharField(max_length=64, blank=True, null=True)
    url = models.URLField(max_length=256, blank=True, null=True)
    image = models.ImageField( blank=True, null=True, upload_to='socials')

    def __str__(self):
        return f"{ self.custom_user } {self.name}"
