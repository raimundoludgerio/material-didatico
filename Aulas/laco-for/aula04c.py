soma = 0
maior = -100000
for c in range(0,4):
    numero = int(input("Informe um número: "))
    if numero > maior:
        maior = numero
    soma = soma + numero

media = soma / 4
print(media)
print(maior)