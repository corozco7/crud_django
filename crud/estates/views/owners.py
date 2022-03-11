"""Owners Views."""

# Django
from pyexpat import model
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Model
from crud.estates.models import Owner

# Forms
from ..forms import OwnerForm


class OwnerListView(ListView):
    """Return the list of owners."""
    template_name = 'owners/list.html'
    model = Owner
    context_object_name = 'owners'


class CreateOwnerView(CreateView):
    """Create a new owner."""
    template_name = "owners/new.html"
    form_class = OwnerForm
    success_url = reverse_lazy("owners:list")


class DetailOwnerView(DetailView):
    """Detail the info of an owner."""
    template_name = "owners/detail.html"
    queryset = Owner.objects.all()
    context_object_name = "owner"


class UpdateOwnerView(UpdateView):
    """Update an owner."""
    template_name = "owners/update.html"
    model = Owner
    form_class = OwnerForm
    success_url = reverse_lazy("owners:list")


class DeleteOwnerView(DeleteView):
    """Delete an owner."""
    template_name = "owners/delete.html"
    model = Owner
    success_url = reverse_lazy("owners:list")
