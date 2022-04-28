# Generated by Django 3.2 on 2022-04-21 15:25

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities_light', '0011_auto_20220420_0745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre del propietario')),
                ('document_type', models.CharField(choices=[('CC', 'Cedula de Ciudadania'), ('NITP', 'Nit persona natural'), ('NITJ', 'Nit persona juridica')], default='NITJ', max_length=4, verbose_name='tipo de documento')),
                ('document_number', models.CharField(max_length=150, unique=True, verbose_name='Numero de Documento')),
                ('address', models.CharField(max_length=100, verbose_name='Direccion')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Telefono')),
                ('email', models.EmailField(blank=True, max_length=150, null=True, verbose_name='Correo Electronico')),
            ],
        ),
        migrations.CreateModel(
            name='Terrain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('area', models.PositiveIntegerField(verbose_name='Area del terreno')),
                ('value', models.PositiveIntegerField(verbose_name='Valor comercial')),
                ('terrain_type', models.CharField(choices=[('UR', 'Urbano'), ('RU', 'Rural')], default='RU', max_length=2, verbose_name='tipo de documento')),
                ('water_source', models.BooleanField(verbose_name='¿Fuente de agua cerca?')),
            ],
        ),
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre del predio')),
                ('estate_number', models.CharField(max_length=100, unique=True, verbose_name='Numero predial')),
                ('value', models.PositiveIntegerField(verbose_name='Avaluo')),
                ('city', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.region', verbose_name='Departamento'), chained_model_field='Region', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.city', verbose_name='Municipio')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.region', verbose_name='Departamento')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estates.owner', verbose_name='Propietario')),
                ('terrain', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='estates.terrain', verbose_name='Terreno')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_floors', models.PositiveIntegerField(verbose_name='Numero de pisos')),
                ('area', models.PositiveIntegerField(verbose_name='Area de la construccion')),
                ('address', models.CharField(max_length=150, verbose_name='Direccion')),
                ('building_type', models.CharField(choices=[('IN', 'Industrial'), ('CO', 'Comercial'), ('RE', 'Residencial')], default='RE', max_length=2, verbose_name='Tipo de construccion')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estates.estate', verbose_name='Predio al que pertenece')),
            ],
        ),
    ]
