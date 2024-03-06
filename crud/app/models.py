from django.db import models

# Create your models here.
class reg(models.Model):
    Name=models.CharField(max_length=20,default="")
    Age=models.IntegerField(default="")
    Email=models.CharField(max_length=20,default="")