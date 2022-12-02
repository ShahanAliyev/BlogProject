# Generated by Django 4.1.3 on 2022-12-01 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_alter_blog_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Category_images')),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Blog_images'),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='Core.category'),
        ),
    ]