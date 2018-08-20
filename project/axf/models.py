from django.db import models


# Create your models here.
#滚动数据
class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=20)
    isDetele = models.BooleanField(default=False)
#导航数据
class Nav(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
#必买数据
class Mustbuy(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=20)
    isDetele = models.BooleanField(default=False)
#便利店数据
class Shop(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=20)
    isDetele = models.BooleanField(default=False)
#主要商品
class Mainshow(models.Model):
    trackid = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=150)
    category_id = models.IntegerField(default=1)
    brand_name = models.CharField(max_length=32)

    img1 = models.CharField(max_length=200)
    child_cid1 = models.IntegerField(default=1)
    product_id1 = models.IntegerField(default=1)
    long_name1 = models.CharField(max_length=128)
    price1 = models.FloatField(default=0)
    market_price1 = models.FloatField(default=0)

    img2 = models.CharField(max_length=200)
    child_cid2 = models.IntegerField(default=1)
    product_id2 = models.IntegerField(default=1)
    long_name2 = models.CharField(max_length=128)
    price2 = models.FloatField(default=0)
    market_price2 = models.FloatField(default=0)

    img3 = models.CharField(max_length=200)
    child_cid3 = models.IntegerField(default=1)
    product_id3 = models.IntegerField(default=1)
    long_name3 = models.CharField(max_length=128)
    price3 = models.FloatField(default=0)
    market_price3 = models.FloatField(default=0)


