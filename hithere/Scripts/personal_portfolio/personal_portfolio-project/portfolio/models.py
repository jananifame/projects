from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=200)
    imagess = models.ImageField(upload_to= 'image',default=False)
    urls = models.URLField(blank=True)
