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


# Solução 2. Desenvolvida por: Julia de Souza Soares

#Ler 3 valores (considere que não serão informados valores iguais) e escrever o maior deles.

# Leitura dos três valores
valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
valor3 = int(input("Informe o terceiro valor: "))

# Encontrando o maior valor
maior_valor = valor1

if valor2 > maior_valor:
  maior_valor = valor2

elif valor3 > maior_valor:
  maior_valor = valor3

# Imprimindo o maior valor
print("O marior valor é:", maior_valor)