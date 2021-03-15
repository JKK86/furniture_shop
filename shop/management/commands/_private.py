from faker import Factory
from slugify import slugify
import random

from shop.models import Product, Category, Wood


def create_name():
    fake = Factory.create("pl_PL")
    categories =['Komoda', 'Krzesło', 'Mebel do ogrodu', 'Łóżko', 'Meblościanka', 'Półka', 'Stół', 'Szafka', 'Szafa']
    return random.choice(categories) + " " + fake.first_name()


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
        category = Category.objects.filter(name__startswith=name[0:2])[0]
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
