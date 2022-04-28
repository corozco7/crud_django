"""Buildings models."""

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Models
from .estates import Estate


class Building(models.Model):
    """Building model."""

    estate = models.ForeignKey(
        Estate,
        on_delete=models.CASCADE,
        verbose_name="Predio al que pertenece"
    )
    num_floors = models.PositiveIntegerField(verbose_name="Numero de pisos")
    area = models.PositiveIntegerField(verbose_name="Area de la construccion")
    address = models.CharField(max_length=150, verbose_name="Direccion")
    class BuildingTypeOptions(models.TextChoices):
        INDUSTRIAL = "IN", _("Industrial")
        COMMERCIAL = "CO", _("Comercial")
        RESIDENTIAL = "RE", _("Residencial")
    building_type = models.CharField(
        max_length=2,
        choices=BuildingTypeOptions.choices,
        default=BuildingTypeOptions.RESIDENTIAL,
        verbose_name="Tipo de construccion"
    )