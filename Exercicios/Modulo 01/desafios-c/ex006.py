"""
    Questão 06: Programa que informa qual número é maior.

    Solução feita por: Mynd Lynx Gomes de Morais
"""
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

# Maior
if n1 >= n2 and n1 >= n3:
  print(f'{n1} é o maior.')
elif n2 >= n1 and n2 >= n3:
  print(f'{n2} é o maior')
else:
  print(f'{n3} é o maior.')

# Menor
if n1 <= n2 and n1 <= n3:
  print(f'{n1} é o menor.')
elif n2 <= n1 and n2 <= n3:
  print(f'{n2} é o menor.')
else:
  print(f'{n3} é o menor.')