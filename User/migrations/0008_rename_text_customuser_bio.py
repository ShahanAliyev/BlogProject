# Generated by Django 4.1.3 on 2022-12-02 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_customuser_text_customuser_work_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='text',
            new_name='bio',
        ),
    ]