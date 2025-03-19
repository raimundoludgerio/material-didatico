from math import ceil, sqrt
import emoji

numero = input("Informe um valor:  ")
print(emoji.emojize("Algo na tela :grinning_face:"))
if numero.isnumeric():
    raizFloat = float(numero)
    resultado = sqrt(raizFloat)
    cosseno = ceil(resultado)
    print(f"A raiz de {numero} é {resultado}")
    print(f"O cosseno de {numero} é {cosseno}")



# raiz = numero**(1/2)
# raiz = math.sqrt(numero)
#
# print(f"A raiz do numero {numero} é {raiz:.2f}!")
# Efetuar a utilização do módulo Math
# Efetuar a utilzação do módulo Random
# Módulos que já vem por padrão e módulos externos: emojis
# Quantidade de módulos disponíveis