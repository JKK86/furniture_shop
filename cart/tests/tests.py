import pytest

from cart.models import CartProduct, Cart


@pytest.mark.django_db
def test_detail_cart(client, create_test_user, create_cart):
    user = create_test_user
    cart = create_cart
    items = cart.cartproduct_set.all()
    response = client.get('/cart/')
    assert response.status_code == 200
    assert len(response.context['cart']) == len(cart)
    assert response.context['cart'].total_price == sum([item.quantity * item.product.price for item in items])


@pytest.mark.django_db
def test_cart_add_product(client, create_product, create_test_user):
    user = create_test_user
    product = create_product
    client.login(username='Test_user', password='test')
    response = client.post(f'/cart/add/{product.id}/', {
        'quantity': 2,
        'override_quantity': False,
    })
    cart_created = Cart.objects.get(user=user)
    assert cart_created
    item_created = CartProduct.objects.get(cart=cart_created, product=product)
    assert item_created
    assert item_created.quantity == 2
    assert response.status_code == 302


@pytest.mark.django_db
def test_cart_remove_product(client, create_test_user, create_cart):
    user = create_test_user
    cart = create_cart
    product = cart.cartproduct_set.first().product
    response = client.post(f'/cart/remove/{product.id}/')
    assert response.status_code == 302
    product_ids = [item.product.id for item in cart.cartproduct_set.all()]
    assert product.id not in product_ids
