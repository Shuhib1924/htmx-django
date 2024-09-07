from django import forms


class Form_required(forms.Form):
    email = forms.CharField()
    name = forms.CharField(min_length=5)
    color = forms.CharField()
