# numero = int(input("Informe um número: "))

# for i in range(1, 11):
#     print(f"{numero} x {i} = {numero * i}")


quadrados = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



palavra = input("informe uma palavra: ")
encontrou_vogal = False

for letra in palavra:
    if letra.lower() in 'aeiou':
        print(f"Vogal encontrada: {letra}")
        encontrou_vogal = True
        break
print(f"Última letra verificada: {letra}")