# Generated by Django 3.1.3 on 2021-05-26 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_categorys_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='user_name',
        ),
    ]
