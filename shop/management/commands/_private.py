from faker import Factory
from slugify import slugify
import random

from shop.models import Product, Category, Wood


def create_name():
    fake = Factory.create("pl_PL")
    categories = Category.objects.all()
    categories = [category.name.split()[0] for category in categories]
    for category in categories:
        if category == 'Stoły':
            category = 'Stół'
        if category == 'Meble':
            category = 'Mebel do ogrodu'
        if category[-1] == 'y' or category[-1] == 'i':
            category[-1] = 'a'
        elif category[-1] == 'a':
            category[-1] = 'o'

    return random.choice(categories) + fake.first_name()


def create_products():
    fake = Factory.create("pl_PL")
    categories = Category.objects.all()
    woods = Wood.objects.all()
    for i in range(1, 50):
        name = create_name()
        slug = slugify(name)
        description = fake.paragraph(nb_sentences=5)
        price = random.randint(50, 3000)
        stock = random.randint(1, 300)
        width = random.randint(50, 300)
        depth = random.randint(20, 160)
        height = random.randint(20, 280)
        category = Category.objects.filter(name__startswith=name[0:1])[0]
        wood = random.choice(woods)
        Product.objects.create(name=name,
                               slug=slug,
                               description=description,
                               price=price,
                               stock=stock,
                               width=width,
                               depth=depth,
                               height=height,
                               category=category,
                               wood=wood)
