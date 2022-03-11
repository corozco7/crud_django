"""Estates views."""

# Django
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'estates/main.html'