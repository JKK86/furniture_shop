from decimal import Decimal

import pytest

from cart.models import Cart
from coupon.models import Coupon


@pytest.mark.django_db
def test_coupon_apply(client, create_cart, create_test_user, create_coupon):
    user = create_test_user
    coupon = create_coupon
    cart_before = create_cart
    total_price = cart_before.get_total_price()
    response = client.post('/coupon/apply/', {
        'code': "TEST",
    })
    cart = Cart.objects.get(user=user)
    coupon = Coupon.objects.get(code="TEST")

    assert response.status_code == 302
    assert cart.get_discount() == (coupon.discount / Decimal('100'))*total_price
    assert cart.get_total_price_with_discount() == total_price - cart.get_discount()
    assert cart.coupon == coupon
