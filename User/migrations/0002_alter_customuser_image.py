# Generated by Django 4.1.3 on 2022-12-02 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='media/static/images/admin-photo_1.jpg', null=True, upload_to='user-images'),
        ),
    ]
