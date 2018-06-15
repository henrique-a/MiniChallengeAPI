from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=50, default="")
    howToPrepare = models.TextField(default="")
    timeToPrepare = models.IntegerField(default=1)
    portions = models.IntegerField(default=1)

    def __str__(self):
        return self.name

class Ingridient(models.Model):
    description = models.CharField(max_length=50, default="")
    quantity = models.FloatField(default=1.0)
    unity = models.CharField(max_length=20, default="")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.description

