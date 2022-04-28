"""Estates URLs."""

# Django
from django.urls import path

# Views
from crud.estates.views import estates as estates_views


urlpatterns = [
    path(
        route='',
        view=estates_views.MainView.as_view(),
        name='main'
    ),
    path(
        route="estates/",
        view=estates_views.EstateListView.as_view(),
        name="list"
    ),
    path(
        route="estates/create/",
        view=estates_views.CreateEstateView.as_view(),
        name="create"
    ),
    path(
        route="estates/<int:pk>/",
        view=estates_views.DetailEstateView.as_view(),
        name="detail"
    ),
    path(
        route="estates/<int:pk>/update",
        view=estates_views.UpdateEstateView.as_view(),
        name="update"
    ),
    path(
        route="estates/<int:pk>/delete",
        view=estates_views.DeleteEstateView.as_view(),
        name="delete"
    ),
]