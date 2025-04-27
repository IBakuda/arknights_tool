
from rest_framework import serializers

from .models import StoryCost


class StoryCostSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = StoryCost
        fields = '__all__'