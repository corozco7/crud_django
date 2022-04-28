"""Estates views."""

# Django
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, ListView, UpdateView, DeleteView

# Models
from ..models import Estate

# Forms
from ..forms import EstateForm


class MainView(TemplateView):
    template_name = 'estates/main.html'


class EstateListView(ListView):
    """Return the list of estates."""
    template_name = "estates/list.html"
    model = Estate
    context_object_name = "estates"


class CreateEstateView(CreateView):
    """Create a new estate."""
    template_name = "estates/new.html"
    form_class = EstateForm
    success_url = reverse_lazy("estates:list")


class DetailEstateView(DetailView):
    """Detail the info of an estate."""
    template_name = "estates/detail.html"
    queryset = Estate.objects.all()
    context_object_name = "estate"


class UpdateEstateView(UpdateView):
    """Update an estate"""
    template_name = "estates/update.html"
    model = Estate
    form_class = EstateForm
    success_url = reverse_lazy("estates:list")


class DeleteEstateView(DeleteView):
    """Delete an estate."""
    template_name = "estates/delete.html"
    model = Estate
    success_url = reverse_lazy("estates:list")