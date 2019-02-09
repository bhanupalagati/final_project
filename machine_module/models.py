from django.db import models

# Create your models here.
class dataInput(models.Model):
    data = models.TextField(max_length = 10000)
