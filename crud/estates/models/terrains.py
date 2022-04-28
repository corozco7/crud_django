"""Terrains models."""

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Terrain(models.Model):
    """Terrain model."""

    id = models.BigAutoField(
        auto_created=True,
        primary_key=True,
        serialize=False
    )

    area = models.PositiveIntegerField(verbose_name="Area del terreno")
    value = models.PositiveIntegerField(verbose_name="Valor comercial")

    class TerrainTypeOptions(models.TextChoices):
        URBAN = "UR", _("Urbano")
        RURAL = "RU", _("Rural")

    terrain_type = models.CharField(
        max_length=2,
        choices=TerrainTypeOptions.choices,
        default=TerrainTypeOptions.RURAL,
        verbose_name="tipo de documento"
    )
    water_source = models.BooleanField(verbose_name="¿Fuente de agua cerca?")

    def __str__(self):
        return f"Lote {self.id}"
