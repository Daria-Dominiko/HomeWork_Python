import requests

basic_url = 'https://yougile.com/api-v2'


def get_api_key():
    params_my = {
        'login': 'вставить данные',
        'password': '',
        'name': 'Поток_100'
    }
    header = {'Content-Type': 'application/json'}

    response = requests.post(basic_url + '/auth/companies', json=params_my,
                             headers=header)
    company_data = response.json()
    company_id = company_data['content'][0]['id']

    params_of_api_key = {
        'login': '',
        'password': '',
        "companyId": company_id
    }

    respons = requests.post(basic_url + '/auth/keys', json=params_of_api_key,
                            headers=header)
    api_key_JS = respons.json()
    return f"Bearer {api_key_JS['key']}"


API_KEY = get_api_key()
PROJECT_ID = None


def test_create_project():
    global PROJECT_ID

    header = {
        'Content-Type': 'application/json',
        'Authorization': API_KEY
    }
    params_my = {
        'title': 'Мой тестовый проект'
    }

    response = requests.post(basic_url + '/projects', json=params_my,
                             headers=header)
    assert response.status_code == 201

    project_data = response.json()
    PROJECT_ID = project_data['id']


def test_get_project():
    header = {
        'Content-Type': 'application/json',
        'Authorization': API_KEY
    }

    response = requests.get(f"{basic_url}/projects/{PROJECT_ID}",
                            headers=header)
    assert response.status_code == 200


def test_update_project():
    header = {
        'Content-Type': 'application/json',
        'Authorization': API_KEY
    }

    update_data = {
        'title': 'Новое название проекта'
    }

    response = requests.put(f"{basic_url}/projects/{PROJECT_ID}",
                            json=update_data,
                            headers=header)
    assert response.status_code == 200


def test_create_project_empty_body():
    header = {
        'Content-Type': 'application/json',
        'Authorization': API_KEY
    }

    response = requests.post(basic_url + '/projects',
                             json={},
                             headers=header)

    assert response.status_code == 400


def test_get_project_nonexistent_id():
    header = {
        'Content-Type': 'application/json',
        'Authorization': API_KEY
    }

    nonexistent_id = '00000000-0000-0000-0000-000000000000'

    response = requests.get(f"{basic_url}/projects/{nonexistent_id}",
                            headers=header)

    assert response.status_code == 404


def test_update_project_invalid_id():
    header = {
        'Content-Type': 'application/json',
        'Authorization': API_KEY
    }

    invalid_id = 'invalid-project-id-123'

    update_data = {
        'title': 'Новое название проекта'
    }

    response = requests.put(f"{basic_url}/projects/{invalid_id}",
                            json=update_data,
                            headers=header)

    assert response.status_code == 404
