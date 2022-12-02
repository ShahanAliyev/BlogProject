from django.contrib import admin
from .models import CustomUser, Social

admin.site.register(CustomUser)
admin.site.register(Social)

# Register your models here.
