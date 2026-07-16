try:
    numero1 = float(input("Informe o primeiro número: "))
    numero2 = float(input("Informe o segundo número: "))
    divisao = numero1 / numero2
    print(divisao)
except ValueError:
    print("Entrada inválida, tente novamente")
except ZeroDivisionError:
    print("Impossível dividir por zero")
