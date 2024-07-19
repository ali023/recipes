from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=50)
    ingredients = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
class Random(models.Model):
    dish = models.CharField(max_length=25)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.dish