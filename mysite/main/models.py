from pyexpat import model
from django.db import models

class Cafe(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}:{self.content}'