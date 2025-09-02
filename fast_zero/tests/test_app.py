from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_doente_deve_retornar_created_e_doente():
    client = TestClient(app)

    response = client.post('/doentes/', json={
        'numero_processo': 456,
        'nome': 'John Doe',
        'data_nascimento': '1990-01-01',
        'genero': 'M',
        'morada': '123 Main St'
    })

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'nome': 'John Doe',
        'morada': '123 Main St'
    }
