def test_register_user(client):
    user_data = {
        'username': 'Wyll',
        'password': '_prideofthegate_',
    }
    response = client.post(
        '/auth/register/',
        json=user_data,
        )
    assert response.status_code == 200
    assert response.json()['detail'] == 'User added successfully'


def test_register_user_username_taken(client):
    user_data = {
        'username': 'Wyll',
        'password': '_prideofthegate_',
    }
    response = client.post(
        '/auth/register/',
        json=user_data,
        )
    assert response.status_code == 400
    assert response.json()['detail'] == 'User already exists'


def test_login_successfully(client):
    user_data = {
        'username': 'Wyll',
        'password': '_prideofthegate_',
    }
    response = client.post(
        '/auth/login/',
        data=user_data,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        )
    assert response.status_code == 200
    assert 'access_token' in response.json()


def test_login_unauthorized(client):
    user_data = {'username': 'Gortash', 'password': 'edictofBane'}
    response = client.post(
        '/auth/login/',
        data=user_data,
        headers={'Content-Type': 'application/x-www-form-urlencoded'},
        )
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid credentials"
