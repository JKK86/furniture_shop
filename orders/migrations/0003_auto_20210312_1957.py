# Generated by Django 3.1.7 on 2021-03-12 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_auto_20210309_1353'),
        ('orders', '0002_auto_20210312_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=6, verbose_name='Cena'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='address',
            field=models.CharField(max_length=255, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='city',
            field=models.CharField(max_length=64, verbose_name='Miasto'),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='postal_code',
            field=models.CharField(max_length=6, verbose_name='Kod pocztowy'),
        ),
        migrations.AlterField(
            model_name='deliveryaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik'),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data dodania'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('OD', 'Odbiór osobisty'), ('KR', 'Dostawa kurierem'), ('PO', 'Dostawa pocztą')], default='OD', max_length=2, verbose_name='Dostawa'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.deliveryaddress', verbose_name='Adres dostawy'),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='Opłacone'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='orders.OrderItem', to='shop.Product', verbose_name='Produkty'),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Data modyfikacji'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Użytkownik'),
        ),
    ]
