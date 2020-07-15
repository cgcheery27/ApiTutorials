from django.db import models


# Create your models here.

class User(models.Model):
    eid = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name
