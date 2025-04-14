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