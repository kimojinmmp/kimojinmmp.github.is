# Generated by Django 3.1.3 on 2021-05-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('number', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
