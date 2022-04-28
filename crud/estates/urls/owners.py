"""Owners URLs."""

# Django
from django.urls import path

# Views
from ..views import owners as owners_views


urlpatterns = [
    path(
        route="",
        view=owners_views.OwnerListView.as_view(),
        name="list"
    ),
    path(
        route="create/",
        view=owners_views.CreateOwnerView.as_view(),
        name="create"
    ),
    path(
        route="<int:pk>/",
        view=owners_views.DetailOwnerView.as_view(),
        name="detail"
    ),
    path(
        route="<int:pk>/update",
        view=owners_views.UpdateOwnerView.as_view(),
        name="update"
    ),
    path(
        route="<int:pk>/delete",
        view=owners_views.DeleteOwnerView.as_view(),
        name="delete"
    ),
]