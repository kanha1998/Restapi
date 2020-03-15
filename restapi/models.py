from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    rating = models.CharField(max_length=60)
    def __str__(self):
        return self.title

