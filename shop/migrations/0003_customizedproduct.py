# Generated by Django 3.1.7 on 2021-09-13 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0002_auto_20210309_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomizedProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nazwa')),
                ('slug', models.SlugField(blank=True, max_length=128)),
                ('description', models.TextField(verbose_name='Opis')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, verbose_name='Cena')),
                ('file', models.FileField(blank=True, upload_to='files', verbose_name='Plik')),
                ('color', models.CharField(choices=[('Natural', 'Naturalny'), ('#935B2A', 'Dąb jasny'), ('#381A10', 'Dąb ciemny'), ('#B35D32', 'Mahoń'), ('White', 'Biel'), ('#5F311B', 'Orzech'), ('#444213', 'Zieleń'), ('#C37437', 'Oranż'), ('Black', 'Czerń')], default='Natural', max_length=8, verbose_name='Kolor')),
                ('width', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Szerokość')),
                ('depth', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Głębokość')),
                ('height', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Wysokość')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Data modyfikacji')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customized_products', to='shop.category', verbose_name='Kategoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Klient')),
                ('wood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.wood', verbose_name='Rodzaj drewna')),
            ],
            options={
                'verbose_name': 'produkt na zamówienie',
                'verbose_name_plural': 'Produkty na zamówienie',
                'ordering': ('created',),
            },
        ),
    ]