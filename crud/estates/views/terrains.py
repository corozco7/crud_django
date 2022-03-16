"""Terrains views."""

# Django
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Models
from ..models import Terrain

# Forms
from ..forms import TerrainForm


class TerrainListView(ListView):
    """Return the list of terrains."""
    template_name = 'terrains/list.html'
    model = Terrain
    context_object_name = 'terrains'


class CreateTerrainView(CreateView):
    """Create a new terrain."""
    template_name = "terrains/new.html"
    form_class = TerrainForm
    success_url = reverse_lazy("terrains:list")


class DetailTerrainView(DetailView):
    """Detail the info of a terrain."""
    template_name = "terrains/detail.html"
    queryset = Terrain.objects.all()
    context_object_name = "terrain"


class UpdateTerrainView(UpdateView):
    """Update a terrain."""
    template_name = "terrains/update.html"
    model = Terrain
    form_class = TerrainForm
    success_url = reverse_lazy("terrains:list")


class DeleteTerrainView(DeleteView):
    """Delete a terrain."""
    template_name = "terrains/delete.html"
    model = Terrain
    success_url = reverse_lazy("terrains:list")