import requests
from bs4 import BeautifulSoup


def validar_crm(crm, uf):
    url = "https://portal.cfm.org.br/index.php?option=com_medicos"
    params = {
        "view": "buscamedicos",
        "task": "buscamedicos",
        "crm": crm,
        "uf": uf
    }

    response = requests.get(url, params=params)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')

    resultado = soup.find("div", class_="resultado-busca")
    print(resultado)
    if resultado:
        return resultado.text.strip()
    return "CRM não encontrado ou erro na consulta"


# Exemplo:
print(validar_crm("152", "PB"))