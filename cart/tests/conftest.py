import pytest

from django.contrib.auth.models import User

from cart.models import Cart, CartProduct
from shop.tests.conftest import set_up


@pytest.fixture
def create_test_user():
    return User.objects.create_user('Test_user', 'user@test.com', 'test')


@pytest.fixture
def create_product(set_up):
    return set_up[1][0]


@pytest.fixture
def create_cart(client, set_up, create_test_user):
    products = set_up[1]
    user = create_test_user
    client.login(username='Test_user', password='test')
    cart = Cart.objects.create(user=user)
    for product in products:
        CartProduct.objects.create(product=product, cart=cart, quantity=1)
    return cart
