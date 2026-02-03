from django.db import models

# Create your models here.


class receipe(models.Model):
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField(max_length=1000)
    receipe_image = models.ImageField(upload_to='receipe/')

