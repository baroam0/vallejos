# Generated by Django 2.2.8 on 2020-06-28 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0003_auto_20200621_0008'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='material',
            unique_together={('descripcion', 'marca_comercial')},
        ),
    ]
