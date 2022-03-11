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
    )
]