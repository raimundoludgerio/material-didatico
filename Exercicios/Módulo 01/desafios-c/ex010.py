"""
    Questão 10: Calculadora entre dois números

    Solução feita por: João Victor Santos Barbosa
"""
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
operacao = int(input('Digite 1. Adição; 2. Subtração; 3. Multiplicação; 4. Divisão: '))

if operacao == 1:
    somar = n1 + n2
    print(f'O resultado de {n1} + {n2} = {somar}')
elif operacao == 2:
    subtracao = n1 - n2
    print(f'O resultado de {n1} - {n2} = {subtracao}')
elif operacao == 3:
    multiplicacao = n1 * n2
    print(f'O resultado de {n1} * {n2} = {multiplicacao}')
elif operacao == 4:
    divisao = n1 / n2
    print(f'O resultado de {n1} / {n2} = {divisao}')
else:
    print('Operação Inválida')