"""
    Crie um programa que leia nome, ano de nascimento e carteira de trabalho. 
    Em seguida, cadastre cada valor em um dicionário (com a idade). 
    Caso a carteira de trabalho seja um valor diferente de zero, o programa deve solicitar o ano de contratação e o salário. 
    O programa deve retornar a idade que a pessoa vai se aposentar.
"""
from datetime import datetime
dados = dict()

dados["nome"] = input("Informe seu nome: ")
ano_nascimento = int(input("Informe apenas o ano que você nasceu: "))
dados["idade"] = datetime.now().year - ano_nascimento
dados["ctps"] = int(input("Informe o número da sua carteira de trabalho: (0 - se não tiver) "))
if dados["ctps"] != 0:
    dados["ano_contratacao"] = int(input("Informe o ano que você foi contratado: "))
    dados["tempo_contribuicao"] = datetime.now().year - dados["ano_contratacao"]
    dados["salario"] = float(input('Informe o seu salário: '))
    dados["aposentadoria"] = dados["idade"] + (dados["ano_contratacao"] + 35) - datetime.now().year


print("------" * 30)
print(dados)
for chave, valor in dados.items():
    print(f"A chave {chave} possui o valor {valor}")