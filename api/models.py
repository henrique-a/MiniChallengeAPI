from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50, default="")
    howToPrepare = models.TextField(default="")
    timeToPrepare = models.IntegerField(default=1)
    portions = models.IntegerField(default=1)
    ingridients = models.TextField(default="")

    def __str__(self):
        return self.name
