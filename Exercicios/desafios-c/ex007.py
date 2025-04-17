"""
    Questão 07: Programa que calcula o passagens.

    Desenvolvida por: <name>
"""

distancia = float(input('Distância da viagem: '))
preco = 0

if distancia <= 200:
    preco = distancia * 0.50
    print(f'O preço da passagem é de R${preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'O preço da passagem é de R${preco:.2f}')