from django.db import models

class Cafe(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f'{self.name}:{self.content}'