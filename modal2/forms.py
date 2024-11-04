from django import forms

STATUS_CHOICES = (("AVAILABLE", "AVAILABLE"), ("NOT AVAILABLE", "NOT AVAILABLE"))


class BookForm(forms.Form):

    title = forms.CharField(
        label="Title", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    author = forms.CharField(
        label="Author", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    status = forms.ChoiceField(
        label="Status",
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    year = forms.CharField(
        label="Year", widget=forms.NumberInput(attrs={"class": "form-control"})
    )
