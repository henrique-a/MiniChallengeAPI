from django.contrib import admin
from .models import Recipe, Ingridient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingridient)