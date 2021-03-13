from django.core.management.base import BaseCommand
from ._private import create_products

from shop.models import Product, Category, Wood


class Command(BaseCommand):
    help = 'Generate random products'

    def handle(self, *args, **options):
        create_products()
        self.stdout.write(self.style.SUCCESS("Succesfully generated 50 products"))
