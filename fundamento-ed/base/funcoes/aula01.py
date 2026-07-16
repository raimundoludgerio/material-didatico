def calcular_area_retangulo(*numeros):
    area = numeros[0] * numeros[1]
    return area


def somar(numero1, numero2):
    return numero1 + numero2


def numero_par(numero):
    return numero % 2 == 0


def saudacao(nome):
    print(f" olá, {nome}! Seja (a).")


def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def contador(*numeros):
    return len(numeros)


print(contador(5,6,7))
print(contador(5,6,7,8,0,2,True))
print(contador(5,6))