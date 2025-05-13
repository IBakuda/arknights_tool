from django import forms

class SerchResoursesForm(forms.Form):
    operator_name = forms.CharField()