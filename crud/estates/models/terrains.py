"""Terrains models."""

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Terrain(models.Model):
    """Terrain model."""

    area = models.PositiveIntegerField(verbose_name="Area del terreno")
    value = models.PositiveIntegerField(verbose_name="Valor comercial")
    water_source = models.BooleanField(verbose_name="¿Fuente de agua cerca?")

    class TerrainTypeOptions(models.TextChoices):
        URBAN = "UR", _("Urbano")
        RURAL = "RU", _("Rural")

    terrain_type = models.CharField(
        max_length=2,
        choices=TerrainTypeOptions.choices,
        default=TerrainTypeOptions.RURAL,
        verbose_name="tipo de documento"
    )