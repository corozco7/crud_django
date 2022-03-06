"""Estates models."""

# Django
from django.db import models

# Models
from smart_selects.db_fields import ChainedForeignKey
from .owners import Owner
from .terrains import Terrain


class Estate(models.Model):
    """Estate model"""

    owner = models.ForeignKey(
        Owner,
        on_delete=models.CASCADE,
        verbose_name="Propietario"
    )
    terrain = models.OneToOneField(
        Terrain,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Terreno"
    )
    name = models.CharField(max_length=150, verbose_name="Nombre del predio")
    estate_number = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Numero predial"
    )
    value = models.PositiveIntegerField(verbose_name="Avaluo")
    department = models.ForeignKey(
        "cities_light.Region",
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		verbose_name='Departamento'
    )
    city = ChainedForeignKey(
        "cities_light.City",
        chained_field=department,
        chained_model_field="region",
        show_all=False,
		auto_choose=True,
		sort=True,
		on_delete=models.SET_NULL,
        null=True,
        blank=True,
		verbose_name='Municipio',
    )