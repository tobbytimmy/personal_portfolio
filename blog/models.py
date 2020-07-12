from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    content = models.CharField(max_length = 1000)