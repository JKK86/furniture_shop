import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_registration(client):
    response = client.post('/registration/', {
        'username': 'Test_user',
        'first_name': 'Test_name',
        'last_name': 'Test_surname',
        'email': 'user@test.com',
        'password': 'secret_pasword',
        'password_repeat': 'secret_pasword',
    })
    assert response.status_code == 302
    user = User.objects.get(username="Test_user")
    assert user
    assert user.email == 'user@test.com'


@pytest.mark.django_db
def test_edit_profile(client, create_test_user):
    user = create_test_user
    client.login(username='Test_user', password='test')
    response = client.post('/account/edit_profile/', {
        'first_name': 'John',
        'last_name': 'Smith',
        'email': 'john@test.com',
    })
    assert response.status_code == 302
    user = User.objects.get(username="Test_user")
    assert user.first_name == 'John'
    assert user.last_name == 'Smith'
    assert user.email == 'john@test.com'
