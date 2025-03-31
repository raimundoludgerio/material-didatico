# Estrururas condicionais

# Condição simples
nome = input("Qual o seu nome? ")
if nome == "Raimundo":
    print("Que nome legal!")
print("Olá, seja bem vindo, {}!".format(nome))

# Condicional composta
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Parabéns, você foi aprovado!")
else:
    print("Estude mais!")
print("Aprovado!" if media >= 7 else "Reprovado!")