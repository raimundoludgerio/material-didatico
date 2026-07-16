n = soma = 0
# while n != 999:
#     n = int(input("Informe um número: "))
#     soma += n


while True:
    n = int(input("Informe um número: "))
    if n == 999:
        break
    soma += n
print("A soma vale:", soma)
