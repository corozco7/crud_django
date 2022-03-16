"""Terrains forms."""

# Django
from django import forms

# Models
from ..models import Terrain

class TerrainForm(forms.ModelForm):
    """owner model form."""
    
    class Meta:
        """Form settings."""

        model = Terrain
        fields = "__all__"