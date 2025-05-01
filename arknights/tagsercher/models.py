from django.db import models

# Create your models here.
class Operator(models.Model):
    name = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    rarity = models.IntegerField(default=3)


