from django.db import models

# Create your models here.

class post(models.Model):
    title = models.TextField()
    author = models.TextField()



