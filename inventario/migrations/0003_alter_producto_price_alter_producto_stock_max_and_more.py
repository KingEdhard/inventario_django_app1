# Generated by Django 5.0.5 on 2024-05-07 01:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_producto_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock_max',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='producto',
            name='stock_min',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]