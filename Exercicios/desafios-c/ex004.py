"""
    Questão 04: Informações sobre um número:
    a. Número é ímpar;
    b. Número é múltiplo de 3;
    c. Número é divisor de 102

    Solução desenvolvida por: Mynd Lynx Gomes de Morais
"""

num = int(input('Digite um número: '))

impar = num % 2
if impar != 0:
  print('É ímpar.')

multiplo = num % 3
if multiplo == 0:
  print('É múltiplo de 3.')

divisor = 102 % num
if divisor == 0:
  print('É divisor de 102.')