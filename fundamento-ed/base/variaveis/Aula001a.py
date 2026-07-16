# Crie um programa que leia dois números e mostre a soma entre eles.
n1 = int(input("informe um valor: "))
n2 = int(input("informe outro valor: "))
s = n1 + n2
print("A soma entre {} e {} vale {}".format(n1, n2, s))
if s > 2:
    num = 1 # Variável de escopo
    print("SOMA OK")
print(num)
