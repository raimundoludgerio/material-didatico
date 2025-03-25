# ex010: solicitar um número real
# Solução desenvolvida por: Jennyffer Francisca da Silva
numero = float(input('Digite um número real: '))

#mostra apenas a parte inteira
print(f' Sua parte inteira é {numero:,.0f}')

# Solução utilizando função trunc feita pelo professor
from math import trunc
numero = float(input("Informe um numero: "))
parte_inteira = trunc(numero)
print(f"A parte inteira de {numero} é {parte_inteira}")
