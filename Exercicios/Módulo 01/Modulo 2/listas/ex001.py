r = "s"
lista = []
while r != 'n':
    numero = int(input("Informe um número: "))
    if numero not in lista:
        lista.append(numero)
    r = input("Deseja continuar [s|n] ").lower()

print(f"Os números digitados foram: {sorted(lista)}")
