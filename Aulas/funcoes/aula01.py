def calcular_area_retangulo(largura, altura):
    area = largura * altura
    return area

def somar(numero1, numero2):
    return numero1 + numero2

def numero_par(numero):
    return numero % 2 == 0


def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a).")


def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def contador(*numeros):
    return len(numeros)

print(contador(2,5,6,1,2))
print(contador(1,10,9))
print(contador(7,2,1,5))
