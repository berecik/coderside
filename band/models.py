from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=1024, null=False, blank=False, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
