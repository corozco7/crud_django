"""Owners forms."""

# Django
from django import forms

# Models
from ..models import Owner


class OwnerForm(forms.ModelForm):
    """Owner model form."""

    class Meta:
        """Form settings."""

        model = Owner
        fields = "__all__"
    
    def clean(self):
        data = super().clean()

        if not data["document_number"].isdigit():
            raise forms.ValidationError("El documento no puede contener letras")
        
        return data