from django.db import models


# Create your models here.
class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=20)
    isDetele = models.BooleanField(default=False)
