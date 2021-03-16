import pytest

from shop.models import Product, Category


@pytest.mark.django_db
def test_list_products(client, set_up):
    response = client.get('/')
    assert response.status_code == 200
    assert len(set_up[1]) == len(response.context['products'])
    assert len(set_up[0]) == len(response.context['categories'])

    # assert Product.objects.count() == len(response.context['products'])
    # assert Category.objects.count() == len(response.context['categories'])

    # assert response.context['products'][0] == set_up[1][0]
    # assert response.context['products'][1] == set_up[1][1]
    # assert response.context['products'][2] == set_up[1][2]

    # assert response.context['categories'][0] == set_up[0][0]
    # assert response.context['categories'][1] == set_up[0][1]
    # assert response.context['categories'][2] == set_up[0][2]


@pytest.mark.django_db
def test_list_products_by_category(client, set_up):
    category = set_up[0][0]
    response = client.get(f'/{category.slug}/')
    assert response.status_code == 200
    assert category.products.count() == len(response.context['products'])


@pytest.mark.django_db
def test_search_products(client, set_up):
    response = client.get('/search', {'search_product': 'testowy'})
    assert response.status_code == 200
    assert len(set_up[1]) == len(response.context['products'])

    # assert Product.objects.count() == len(response.context['products'])

    response = client.get('/search', {'search_product': 'TESTOWY 1'})
    assert response.status_code == 200
    assert len(response.context['products']) == 1


@pytest.mark.django_db
def test_detail_product(client, set_up):
    product = set_up[1][0]
    response = client.get(f'/{product.id}/{product.slug}/')
    assert response.status_code == 200
    assert response.context['product'] == product
    # assert response.context['product'].name == product.name
    # assert response.context['product'].description == product.description
    # assert response.context['product'].price == product.price
    # assert response.context['product'].stock == product.stock
    # assert response.context['product'].category == product.category
    # assert response.context['product'].wood == product.wood
    # assert response.context['product'].width == product.width
    # assert response.context['product'].depth == product.depth
    # assert response.context['product'].height == product.height
