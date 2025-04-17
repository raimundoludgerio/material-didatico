"""
    Questão 03: Programa que identifica quando um número é par

    Solução desenvolvida por: João Victor Santos Barbosa
"""
Numero = float(input('Digite um número: '))

if (Numero % 2) == 1:
    print(f'O número {Numero} é impar.')
else:
    print(f'O número {Numero} é par.')