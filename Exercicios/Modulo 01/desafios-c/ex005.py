"""
    Questão 05: Saber se o ano é bissexto.

    Solução implementada por: João Victor
"""
ano = int(input('Digite um ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano bissexto.')
else:
    print('Não é um ano bissexto.')