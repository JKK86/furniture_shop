# Generated by Django 3.1.7 on 2021-03-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deliveryaddress',
            options={'ordering': ('user',), 'verbose_name': 'adres dostawy', 'verbose_name_plural': 'Adresy dostawy'},
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('OD', 'Odbiór osobisty'), ('KR', 'Dostawa kurierem'), ('PO', 'Dostawa pocztą')], default='OD', max_length=2),
        ),
    ]
