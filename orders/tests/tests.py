import pytest

from cart.models import CartProduct, Cart
from shop.tests.conftest import set_up

from orders.models import ODBIOR, KURIER, DeliveryAddress
from cart.tests.conftest import create_test_user, create_cart


@pytest.mark.django_db
def test_order_create_without_address(client, create_test_user, create_cart):
    user = create_test_user
    cart = create_cart
    cart_length = len(cart)
    items = cart.cartproduct_set.all()
    response = client.post('/orders/create/', {
        'delivery_type': ODBIOR,
        'address': 'ul. Testowa 1',
        'postal_code': '00-000',
        'city': 'Test'
    })
    assert response.status_code == 200
    cart_cleared = Cart.objects.get(user=user)
    assert cart_cleared.cartproduct_set.count() == 0
    assert response.context['order'].delivery_address is None
    assert sum([item.quantity for item in response.context['order'].orderitem_set.all()]) == cart_length


@pytest.mark.django_db
def test_order_create_with_address(client, create_test_user, create_cart):
    user = create_test_user
    cart = create_cart
    cart_length = len(cart)
    items = cart.cartproduct_set.all()
    response = client.post('/orders/create/', {
        'delivery_type': KURIER,
        'address': 'ul. Testowa 1',
        'postal_code': '00-000',
        'city': 'Test'
    })
    assert response.status_code == 200
    cart_cleared = Cart.objects.get(user=user)
    assert cart_cleared.cartproduct_set.count() == 0
    assert response.context['order'].delivery_address.address == 'ul. Testowa 1'
    assert response.context['order'].delivery_address.postal_code == '00-000'
    assert response.context['order'].delivery_address.city == 'Test'
    assert DeliveryAddress.objects.count() == 1
    assert sum([item.quantity for item in response.context['order'].orderitem_set.all()]) == cart_length
