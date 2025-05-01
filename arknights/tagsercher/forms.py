from django import forms

from .models import Operator


class AddOperatorForm(forms.Form):
    name = forms.CharField(max_length=100)
    tag = forms.CharField(max_length=100)
    rarity = forms.ChoiceField(label="Редкость", choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6")))


class TagChouseForm(forms.Form):
    custom_input = forms.CharField(required=False)
    #Class
    guard = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    sniper = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    defender = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    medic = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    suporter = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    caster = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    specialist = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    vanguard = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    #Position
    melee = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    ranged = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    #Qualification
    starter = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    senior_operator = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    top_operator = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    #Affix
    crowd_control = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    nuker = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    healing = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    support = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    dp_recovery = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    dps = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    aoe = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    defense = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    slow = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    debuff = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    fast_redeploy = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    shift = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    summon = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    robot = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    elemental = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    #Rarity
    all = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    six_star = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    five_star = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    four_star = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    three_star = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    two_star = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    one_star = forms.BooleanField(widget=forms.CheckboxInput, required=False)
