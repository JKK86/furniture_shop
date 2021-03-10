import pytest
import random

from shop.models import Product, Category, Wood


@pytest.fixture
def set_up():
    categories = []
    products = []
    woods = []
    for i in range(5):
        categories.append(Category.objects.create(
            name=f'Kategoria testowa {i}',
            slug=f'kategoria-testowa-{i}'
        ))

    for i in range(3):
        woods.append(Wood.objects.create(
            type=f'Drewno testowe {i}',
            description=f'Opis drewna testowego {i}'
        ))

    for i in range(5):
        products.append(Product.objects.create(
            name=f'Produkt testowy {i}',
            slug=f'produkt-testowy-{i}',
            description=f'Opis produktu testowego {i}',
            price=random.randint(100, 1000),
            stock=random.randint(1, 100),
            width=random.randint(50, 200),
            depth=random.randint(30, 120),
            height=random.randint(50, 200),
            category=random.choice(categories),
            wood=random.choice(woods),
        ))

    return [categories, products]