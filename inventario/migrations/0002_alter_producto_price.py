# Generated by Django 5.0.5 on 2024-05-06 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
