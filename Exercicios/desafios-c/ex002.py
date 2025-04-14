"""
    Questão 02: Programa que informar um número positivo, negativo ou neutro.

    Solução implementada por: João Victor Santos Barbosa
"""
Numero = float(input('Digite um número: '))

if Numero > 0:
    print(f'O número {Numero} é positivo!')
elif Numero < 0:
    print(f'O numero {Numero} é negativo!')
else:
    print(f'O número {Numero} é neutro!')