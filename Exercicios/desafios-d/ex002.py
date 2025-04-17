"""
Qustão 02: Ler 3 valores (considere que não serão informados valores iguais) e
escrever o maior deles.

Solução desenvolvida por: Cauã Alexandre da Silva Barros
"""
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
valor3 = float(input('Digite o terceiro valor: '))
if valor1 > valor2 > valor3:
  print(f'{valor1} (Primeiro valor) É o maior número')
elif valor2 > valor1 > valor3:
  print(f'{valor2} (Segundo valor) É o maior número')
else:
  print(f'{valor3} (Terceiro valor) É o maior número')