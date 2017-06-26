
from django.db import models

# Create your models here.
# 定义书类,继承models.Model
class BookInfo(models.Model):
    # 最大字符串长度20
    btitle=models.CharField(max_length=20)
    # 日期类型
    bpub_data=models.DateField()

    # def __str__(self):
    #     # python3不需要编码，python2则需要加一个编码encode('utf-8')
    #     return self.btitle

# 定义英雄类,继承models.Model
class HeroInfo(models.Model):
    hname=models.CharField(max_length=20)
    hgender=models.BooleanField(default=False)
    hcomment=models.CharField(max_length=100)
    # 让BookInfo类和HeroInfo类之间建立起一对多的关系
    hbook=models.ForeignKey('BookInfo')