from django.db import models

# Create your models here.

class categorys(models.Model):
    category=models.CharField(max_length=20)
    user_name = models.ForeignKey('user.User', on_delete=models.CASCADE)
    cate_img=models.ImageField('照片', upload_to ='upload/img', blank = True, null = True,default="upload/img/others.png")
    class META:
        db_table = 'category'
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category

class content(models.Model):
    title=models.CharField(max_length=30 , unique=True)
    select=models.ForeignKey('categorys',on_delete=models.CASCADE)
    descHtml=models.TextField()
    descMd=models.TextField()
    last_modified_date=models.DateField(auto_now=True)
    class META:
        db_table='tb_content'
        verbose_name='用户数据'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title