from math import ceil, sqrt


numero = input("Informe um valor:  ")
if numero.isnumeric():
    raizFloat = float(numero)
    resultado = sqrt(raizFloat)
    cosseno = ceil(resultado)
    print(f"A raiz de {numero} é {resultado}")
    print(f"O cosseno de {numero} é {cosseno}")

# print(emoji.emojize('Python is :thumbs_up:'))

# raiz = numero**(1/2)
# raiz = math.sqrt(numero)
#
# print(f"A raiz do numero {numero} é {raiz:.2f}!")
# Efetuar a utilização do módulo Math
# Efetuar a utilzação do módulo Random
# Módulos que já vem por padrão e módulos externos: emojis
# Quantidade de módulos disponíveis