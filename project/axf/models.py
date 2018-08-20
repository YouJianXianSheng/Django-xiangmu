from django.db import models


# Create your models here.
# 滚动数据
class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=20)
    isDetele = models.BooleanField(default=False)


# 导航数据
class Nav(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)


# 必买数据
class Mustbuy(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=20)
    isDetele = models.BooleanField(default=False)


# 便利店数据
class Shop(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=20)
    isDetele = models.BooleanField(default=False)


# 主要商品
class Mainshow(models.Model):
    trackid = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=150)
    categoryid = models.IntegerField(default=1)
    brandname = models.CharField(max_length=32)

    img1 = models.CharField(max_length=200)
    childcid1 = models.IntegerField(default=1)
    productid1 = models.IntegerField(default=1)
    longname1 = models.CharField(max_length=128)
    price1 = models.FloatField(default=0)
    marketprice1 = models.FloatField(default=0)

    img2 = models.CharField(max_length=200)
    childcid2 = models.IntegerField(default=1)
    productid2 = models.IntegerField(default=1)
    longname2 = models.CharField(max_length=128)
    price2 = models.FloatField(default=0)
    marketprice2 = models.FloatField(default=0)

    img3 = models.CharField(max_length=200)
    childcid3 = models.IntegerField(default=1)
    productid3 = models.IntegerField(default=1)
    longname3 = models.CharField(max_length=128)
    price3 = models.FloatField(default=0)
    marketprice3 = models.FloatField(default=0)
