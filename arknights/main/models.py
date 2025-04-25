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


class Player(models.Model):
    name = models.CharField()
    orundum = models.IntegerField(default=0)
    originium = models.IntegerField(default=0)
    tickets = models.IntegerField(default=0)


    class Meta():
        pass