"""
    Questão 08: Conversão de bases numéricas

    Solução implementada por: João Victor Santos Barbosa
"""

numero = int(input('Digite um número inteiro: '))
conversao = int(input('Para converter os números digite: 1. Binário, 2. Octal, 3. Hexadecimal: '))

if conversao == 1:
    binario = bin(numero)
    print(f'O número {numero} em binário é {binario}')
elif conversao == 2:
    octal = oct(numero)
    print(f'O número {numero} em octal é {octal}')
elif conversao == 3:
    hexa = hex(numero)
    print(f'O número {numero} em Hexa é {hexa}')
else:
    print('Resultado inválido, tente utilizando uma das opções acima.')
