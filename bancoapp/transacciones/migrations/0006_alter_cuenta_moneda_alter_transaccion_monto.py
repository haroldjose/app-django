# Generated by Django 4.2.6 on 2023-10-07 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacciones', '0005_alter_transaccion_monto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='moneda',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='monto',
            field=models.DecimalField(decimal_places=2, max_digits=100),
        ),
    ]
