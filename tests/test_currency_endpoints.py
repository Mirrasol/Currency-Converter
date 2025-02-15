import pytest


def test_show_currencies_authorized(client):
    user_data = {'username': 'Wyll', 'password': '_prideofthegate_'}
    response_login = client.post('/auth/login/', data=user_data)
    access_token = response_login.json()['access_token']

    authorized_headers = {'Authorization': f'Bearer {access_token}'}
    response = client.get('/currency/list/', headers=authorized_headers)
    assert response.status_code == 200


def test_show_currencies_unauthorized(client):
    with pytest.raises(KeyError):
        user_data = {'username': 'Gortash', 'password': 'edictofBane'}
        response_login = client.post('/auth/login/', data=user_data)
        access_token = response_login.json()['access_token']

        authorized_headers = {'Authorization': f'Bearer {access_token}'}
        response = client.get('/currency/list/', headers=authorized_headers)
        assert response.status_code == 401
        assert response.json()["detail"] == "Not authenticated"


def test_exchange_currency_authorized(client):
    user_data = {'username': 'Wyll', 'password': '_prideofthegate_'}
    response_login = client.post('/auth/login/', data=user_data)
    access_token = response_login.json()['access_token']

    authorized_headers = {'Authorization': f'Bearer {access_token}'}
    exchange_data = {"from_currency": "usd", "to_currency": "cad", "amount": 16}
    response = client.post(
        '/currency/exchange/',
        json=exchange_data,
        headers=authorized_headers,
        )
    assert response.status_code == 200


def test_exchange_currency_unauthorized(client):
    with pytest.raises(KeyError):
        user_data = {'username': 'Gortash', 'password': 'edictofBane'}
        response_login = client.post('/auth/login/', data=user_data)
        access_token = response_login.json()['access_token']

        authorized_headers = {'Authorization': f'Bearer {access_token}'}
        exchange_data = {"from_currency": "usd", "to_currency": "cad", "amount": 16}
        response = client.post(
            '/currency/exchange/',
            params=exchange_data,
            headers=authorized_headers,
            )
        assert response.status_code == 401
        assert response.json()["detail"] == "Not authenticated"


def test_exchange_currency_unsupported_codes(client):
    user_data = {'username': 'Wyll', 'password': '_prideofthegate_'}
    response_login = client.post('/auth/login/', data=user_data)
    access_token = response_login.json()['access_token']

    authorized_headers = {'Authorization': f'Bearer {access_token}'}
    exchange_data = {"from_currency": "gold", "to_currency": "cad", "amount": 16}
    response = client.post(
        '/currency/exchange/',
        params=exchange_data,
        headers=authorized_headers,
        )
    assert response.status_code != 200
