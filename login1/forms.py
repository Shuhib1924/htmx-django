from django import forms
from django.core.validators import RegexValidator
from .models import Car

numeric = RegexValidator(r"^[0-9]*$")


class CarForm(forms.ModelForm):
    make = forms.CharField(required=True, max_length=30)
    model = forms.CharField(required=True, max_length=30)
    year = forms.IntegerField(
        required=True, min_value=1900, max_value=2024, validators=[numeric]
    )

    class Meta:
        model = Car
        fields = "__all__"
