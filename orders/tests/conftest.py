import pytest

from django.contrib.auth.models import User

from orders.models import Order, OrderItem, DeliveryAddress
from shop.tests.conftest import set_up
from cart.tests.conftest import create_test_user


@pytest.fixture
def create_order(client, set_up, create_test_user):
    products = set_up[1]
    user = create_test_user
    orders = []
    client.login(username='Test_user', password='test')
    for i in range(3):
        order = Order.objects.create(user=user)
        for product in products:
            OrderItem.objects.create(product=product, order=order, price=product.price)
        orders.append(order)

    return orders


@pytest.fixture
def create_addresses(client, create_test_user):
    user = create_test_user
    addresses = []
    client.login(username='Test_user', password='test')
    for i in range(3):
        address = DeliveryAddress.objects.create(
            user=user, address=f'ul. Testowa {i}', postal_code=f'00-00{i}', city=f'Test{i}'
        )
        addresses.append(address)

    return addresses
