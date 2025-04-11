from django.db import models


# Create your models here.
class StoryCost(models.Model):
    story_type = models.CharField()
    name = models.CharField()
    total = models.IntegerField()
    normal = models.IntegerField()
    challenge = models.IntegerField()
    extra = models.IntegerField()
    clear = models.BooleanField(default=False)