# Generated by Django 2.2.8 on 2020-06-28 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0006_auto_20200628_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marcacomercial',
            name='descripcion',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]