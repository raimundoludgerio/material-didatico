"""
 Q01: Gerar um número e pedir para
 máquina "pensar" qual foi o número escolhido.

 Solução implementada por: Mynd Lynx Gomes de Morais
"""
from random import randint
ma = randint(0,10)

us = int(input('Advinhe o número escolhido pela máquina: '))
print(f'Número do usuário: {us}')
print(f'Número da máquina: {ma}')

if us == ma:
  print('Correto!')
else:
  print('Incorreto!')


# ------ SEGUNDA SOLÇÃO ------
# DESENVOLVIDA POR: JOAO VICTOR SANTOS BARBOSA

Aleatorio = randint(0,10)
Numero = int(input('Adivinhe o número que está entre 0 a 10: '))

while Aleatorio != Numero:
    if Aleatorio != Numero:
        print('Você errou')
        print(f'Seu número: {Numero}')
        print(f'Número escolhido: {Aleatorio}')
        print('Tente novamente!')
        Numero = int(input('Adivinhe o número que está entre 0 a 10: '))
        Aleatorio = randint(0,10)

print(f'Você acertou!')
print(f'Seu número {Numero}')
print(f'Número escolhido {Aleatorio}')