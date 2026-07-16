import math

import emoji

"""
    Questão 08: Cálculo do empréstimo.
    O empréstimo é aprovado quando as parcelas não ultrapassa 30% do salário.

    Solução desenvolvida por: Bianca Vieira Francelino
    
    PS: Solução atualizada pelo professor com algumas alterações.
"""
valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salario: '))
anos = int(input('Digite os anos que você vai pagar: '))

mes = anos * 12

parcela = valor / mes
limite = salario * 0.3
print(f"\nPara pagar uma casa de R$ {valor:.2f} em {anos} anos,")
print(f"a prestação será de R$ {parcela:.2f} por mês.")
if parcela > limite:
    # Número mínimo de meses necessários para que a parcela fique igual ou abaixo do limite de 30% do salário.
    # Calcula o número mínimo de meses necessários
    meses_necessarios = int(valor / limite) + 1

    # Arredonda pra cima o número de anos com math.ceil
    anos_necessarios = math.ceil(meses_necessarios / 12)

    palavra_ano = "ano" if anos_necessarios == 1 else "anos"
    print(emoji.emojize('Emréstimo não aprovado! :confused_face:'))
    print(f'Para que o valor seja aprovado, deverá ser financiada em mais de {anos_necessarios} {palavra_ano}')
else:
    print(emoji.emojize('Emréstimo aprovado! :beaming_face_with_smiling_eyes: :money_with_wings:'))
    print(f'O valor das parcelas é: R$ {parcela:.2f}')
