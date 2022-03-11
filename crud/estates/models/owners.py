"""Owners models."""

# Django
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Owner(models.Model):
    """Owner model."""

    name = models.CharField(max_length=150, verbose_name="Nombre del propietario")

    class DocumentTypeOptions(models.TextChoices):
        ID = 'CC', _('Cedula de Ciudadania')
        NITP = 'NITP', _('Nit persona natural')
        NITJ = 'NITJ', _('Nit persona juridica')

    document_type = models.CharField(
        max_length=4,
        choices=DocumentTypeOptions.choices,
        default=DocumentTypeOptions.NITJ,
        verbose_name="tipo de documento"
    )

    document_number = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Numero de Documento")
    address = models.CharField(max_length=100, verbose_name="Direccion")
    phone_number = models.CharField(max_length=20,verbose_name="Telefono")
    email = models.EmailField(
		max_length=150,
		null=True,
        blank=True,
		verbose_name="Correo Electronico"
	)
    
    def __str__(self):
        return self.name
    