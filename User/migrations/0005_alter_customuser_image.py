# Generated by Django 4.1.3 on 2022-12-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, default='/admin-photo1.jpg', null=True, upload_to='user-images'),
        ),
    ]
