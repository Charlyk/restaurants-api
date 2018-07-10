from django.contrib import admin

# Register your models here.
from api import models

admin.site.register(models.Restaurant)
admin.site.register(models.Hour)
admin.site.register(models.Photo)
