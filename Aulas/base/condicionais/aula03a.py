from random import randint
opcao = True
while opcao:
    numero_maquina = randint(0, 5)
    numero_usuario = int(input("Informe um número entre 0 e 10: "))
    print(f"Máquina: {numero_maquina}")
    print(f"Usuário: {numero_usuario}")
    if numero_usuario == numero_maquina:
        print("Você acertou!")
        opcao = False
    else:
        print("Que pena, tente novamente")