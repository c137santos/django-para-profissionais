from http import HTTPStatus


def test_home_status_code(client):
    resposta = client.get('/')
    assert resposta.status_code == HTTPStatus.OK


def test_home_status_code_super_teste_do_ruffffffffffffffffffffffffffffffffffffffffffffffff(client):
    resposta = client.get('/')
    assert resposta.status_code == HTTPStatus.OK
