from django.db import models

# Create your models here.
class Config(models.Model):
    url = models.CharField('URL', max_length=300)
    typeauth = models.CharField('Type Auth', max_length=100)