"""Estates forms."""

# Django
from django import forms

# Models
from ..models import Estate


class EstateForm(forms.ModelForm):
    """Estate model form."""

    class Meta:
        model = Estate
        fields = "__all__"