"""
    Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. 
    Em seguida, mostre a listagem de números gerados e também indique qual é o menor, qual é o maior da tupla.
"""

from random import randint

tupla_numeros = (randint(1,20), randint(1,20), randint(1,20), randint(1,20), randint(1,20))
print("Os números gerados foram: ", tupla_numeros)

print("O maior deles foi: ", max(tupla_numeros))

print("O menor deles foi: ", min(tupla_numeros))
