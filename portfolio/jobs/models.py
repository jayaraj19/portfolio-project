from django.db import models


# Create your models here.

class Job(models.Model):
    name = models.CharField(max_length=100, unique=True, default="python")
    img = models.ImageField(upload_to='image/')
    summary = models.CharField(max_length=300)
    link = models.URLField(unique=True)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    certificate = models.ImageField(upload_to='certificates/')
    level = models.CharField(max_length=100,default="intermediate")
