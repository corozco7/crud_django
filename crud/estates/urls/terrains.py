"""Terrains URLs."""

# Django
from django.urls import path

# Views
from ..views import terrains as terrains_views


urlpatterns = [
    path(
        route="",
        view=terrains_views.TerrainListView.as_view(),
        name="list"
    ),
    path(
        route="create/",
        view=terrains_views.CreateTerrainView.as_view(),
        name="create"
    ),
    path(
        route="<int:pk>/",
        view=terrains_views.DetailTerrainView.as_view(),
        name="detail"
    ),
    path(
        route="<int:pk>/update",
        view=terrains_views.UpdateTerrainView.as_view(),
        name="update"
    ),
    path(
        route="<int:pk>/delete",
        view=terrains_views.DeleteTerrainView.as_view(),
        name="delete"
    ),
]