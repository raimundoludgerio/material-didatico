"""
8. Faça um programa que leia o nome e o peso de várias pessoas,
guarde tudo em uma lista e o no final mostre:
a. Quantas pessoas foram cadastradas;
b. Uma listagem com as pessoas mais pesadas;
c. Uma listagem com as pessoas mais leves.
    
"""

r = "s"
lista_peso = []
lista_nome = []
while r != 'n':
    nome = str(input("Informe o nome da pessoa: "))
    peso = float(input("Informe o peso: "))
    lista_nome.append(nome)
    lista_peso.append(peso)
    r = input("Deseja continuar [s|n] ").lower()
print(f"Foram cadastrada: {len(lista_peso)} pessoas")
media = sum(lista_peso)/len(lista_peso)
pessoas_maior_peso = []
pessoas_menos_peso = []
for i in range(len(lista_peso)):
    if lista_peso[i] >= media:
        pessoas_maior_peso.append(lista_nome[i])
    else:
        pessoas_menos_peso.append(lista_nome[i])
print("Média de pesos: ", media)
print(f"Pessoas com Menor peso: {pessoas_menos_peso}")
print(f"Pessoas Maior Peso: {pessoas_maior_peso}")



