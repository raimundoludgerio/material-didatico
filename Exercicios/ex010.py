# Receba um número com ponto flutuante e retorne apenas a parte inteira
from math import trunc
numero = float(input("Informe um numero: "))
parte_inteira = trunc(numero)
print(f"A parte inteira de {numero} é {parte_inteira}")
