# Generated by Django 2.2.8 on 2020-12-28 00:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0003_auto_20201222_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleoperacion',
            name='precio',
        ),
    ]
