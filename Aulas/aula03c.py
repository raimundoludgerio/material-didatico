opcao = str(input('Digite algo: ')).lower()
while not opcao == 'x':
    if opcao == 'a':
        print("Bom dia!")
    elif opcao == 'b':
        print("Boa tarde!")
    elif opcao == 'c':
        print("Boa noite!")
    else:
        print("OPÇÃO INVÁLIDA, TENTE NOVAMENTE")
    opcao = str(input('Digite algo: ')).lower()