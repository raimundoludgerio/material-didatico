print("=" * 15 + " Repetindo várias vezes a mesma mensagem " + "=" * 15)
for c in range(0, 10):
    print("Olá")
print("Fim")

print("Contando de 1 até 5")
# Contando de 1 até 5
for contador in range(1, 6):
    print(" ", contador, end="")
print()
print("Contando de 5 até 1")
# Contando de 5 até 1
for contador in range(5, 0, -1):
    print(" ", contador, end="")
print()
print("Contando apenas os pares de 1 a 20")
# Contando apenas os pares de 1 a 20
for contador in range(0, 21, 2):
    print(" ", contador, end="")
