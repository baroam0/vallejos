# Generated by Django 2.2 on 2020-08-20 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalleoperacion',
            name='operacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operaciones.Operacion'),
        ),
    ]