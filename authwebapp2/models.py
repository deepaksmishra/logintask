from django.db import models
class info(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length=500)
    body = models.CharField(max_length=100)
# Create your models here.
