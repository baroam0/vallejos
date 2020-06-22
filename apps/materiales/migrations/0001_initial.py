# Generated by Django 2.2.8 on 2020-06-20 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaComercial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Marcas Comerciales',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100, unique=True)),
                ('codigo_barra', models.ImageField(upload_to='materiales')),
                ('marca_comercial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiales.MarcaComercial')),
            ],
            options={
                'verbose_name_plural': 'Materiales',
            },
        ),
    ]
