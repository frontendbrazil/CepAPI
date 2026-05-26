import pytest
import requests

BASE_URL = "https://viacep.com.br/ws"


class CepService:

    def __init__(self):
        self.session = requests.Session()

    def consultar(self, cep):
        return self.session.get(f"{BASE_URL}/{cep}/json/")


@pytest.fixture
def service():
    return CepService()


def endereco_valido(dados):

    campos_obrigatorios = [
        "logradouro",
        "bairro",
        "localidade",
        "uf"
    ]

    return all(campo in dados for campo in campos_obrigatorios)

def test_consulta_cep_valido(service):

    response = service.consultar("01001000")

    assert response.status_code == 200

    dados = response.json()

    assert dados["logradouro"] == "Praça da Sé"
    assert dados["bairro"] == "Sé"
    assert dados["localidade"] == "São Paulo"
    assert dados["uf"] == "SP"

@pytest.mark.parametrize("cep", [
    "01001000",
    "01001-000"
])
def test_consulta_cep_formatado(service, cep):

    response = service.consultar(cep)

    assert response.ok
    assert endereco_valido(response.json())

def test_consulta_cep_inexistente(service):

    response = service.consultar("99999999")

    dados = response.json()

    assert response.status_code == 200
    assert dados.get("erro") is True

@pytest.mark.parametrize("entrada", [
    "ABCDEFGH",
    "12345",
    ""
])
def test_consulta_com_entradas_invalidas(service, entrada):

    response = service.consultar(entrada)

    assert response.status_code in [200, 400]