from django import forms

from .models import Expense


class ExpenseForm(forms.ModelForm):
    required_css_class = "required"

    class Meta:
        model = Expense
        fields = ("description", "value")
        widgets = {
            "description": forms.TextInput(
                attrs={"placeholder": "name", "autofocus": True}
            ),
            "value": forms.NumberInput(attrs={"placeholder": "price"}),
        }

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-2 border-red-300"
