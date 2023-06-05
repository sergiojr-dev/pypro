from django.test import Client

def test_status_code(client:Client):
    resp = client.get('/') # está pegando o status da pagina home
    assert resp.status_code == 200