# Generated by Django 3.1.7 on 2021-09-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210920_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customizedproduct',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Cena'),
        ),
    ]