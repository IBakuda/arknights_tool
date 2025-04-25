# forms.py
from django import forms
from .models import StoryCost, Player


class StoryCostForm(forms.ModelForm):
    class Meta:
        model = StoryCost
        fields = ['story_type', 'name', 'total', 'normal', 'challenge', 'extra', 'clear']


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'orundum', 'originium', 'tickets']
