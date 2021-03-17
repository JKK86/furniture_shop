import datetime
import pytz

import pytest

from cart.tests.conftest import create_test_user, create_cart
from shop.tests.conftest import set_up
from coupon.models import Coupon
from sklep_meblowy.settings import TIME_ZONE


@pytest.fixture
def create_coupon():
    coupon = Coupon.objects.create(
        code="TEST",
        valid_from=datetime.datetime(2021, 3, 17, 15, 10, 30, tzinfo=pytz.UTC),
        valid_to=datetime.datetime(2022, 3, 17, 15, 10, 30, tzinfo=pytz.UTC),
        active=True,
        discount=10
    )
    return coupon