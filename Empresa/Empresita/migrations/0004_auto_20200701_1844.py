# Generated by Django 2.2 on 2020-07-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empresita', '0003_auto_20200701_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='descuento',
            field=models.BooleanField(null=True),
        ),
    ]
