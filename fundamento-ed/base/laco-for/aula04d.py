somatorio = 0
for i in range(1, 5):
    numero = int(input("Informe um número: "))
    somatorio += numero
media = somatorio / 4
print("A média foi:", media, "Você foi aprovado")
print("A média foi: {} Você foi aprovado".format(media))
print(f"A média foi: {media} Você foi aprovado")
print(f"A média foi:" + media + "Você foi aprovado")
