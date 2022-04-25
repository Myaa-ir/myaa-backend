from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class WorkShop(models.Model):
    name = models.CharField(max_length=99)

    categories = models.ManyToManyField('category.Category')

    long = models.DecimalField(max_digits=9, decimal_places=6)
    lat = models.DecimalField(max_digits=9, decimal_places=6)

    owner = get_user_model()
    add_time = models.DateTimeField(auto_created=True)
    edit_time = models.DateTimeField(auto_now=True)

class Service(models.Model):
    title = models.CharField(max_length=99)
    categories = models.ManyToManyField('category.Category')
    workshop = models.ForeignKey(WorkShop, on_delete=models.CASCADE)