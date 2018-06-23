from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50, default="")
    howToPrepare = models.TextField(default="")
    timeToPrepare = models.IntegerField(default=0)
    portions = models.IntegerField(default=0)
    image = models.ImageField(null=True, blank=True, upload_to='img')
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Ingridient(models.Model):
    description = models.CharField(max_length=50, default="")
    quantity = models.FloatField(default=0.0)
    unity = models.CharField(max_length=20, default="")
    price = models.FloatField(default=0.0)
    recipe = models.ForeignKey(Recipe, related_name='ingridients', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.description