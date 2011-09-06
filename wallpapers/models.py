from django.db import models

class Category(models.Model):
    """Wallpaper Category Entity"""    
    name = models.CharField(max_length=30, null=False, unique=True)
    alias = models.CharField(max_length=30, null=False, unique=True)
    count = models.IntegerField(default=0, null=False)
