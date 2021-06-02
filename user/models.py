from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=30,unique=True)
    number=models.CharField(max_length=11,unique=True,blank=False)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=20,unique=True,blank=False)
    class META:
        db_table='tb_user'
        verbose_name='用户管理'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name