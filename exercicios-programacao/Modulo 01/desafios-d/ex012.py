"""
    O posto de combustíveis "Abasteça Já" decidiu oferecer uma super
    promoção durante o feriado, com preços abaixo do mercado. Todos os clientes
    que abastecerem mais de 30 litros de etanol ganharão uma troca de óleo
    gratuita. Crie um programa que receba como entrada o tipo de combustível
    escolhido e o valor em dinheiro que o cliente deseja gastar. O programa deve
    calcular o total de combustível abastecido e informar se o cliente ganhou ou
    não a troca de óleo, de acordo com a quantidade de etanol abastecido.
    (Considere R$ 4,13 o Litro de Etanol).

    Solução desenvolvida por: Pedro Guilherme de Freitas Avelino

"""

combustivel = str(input('Qual foi o combustível escolhido? ')).lower()
valor = float(input('Qual o valor a ser pago? '))

quantidade_litros = valor / 4.13
print(f"Esse valor consegue abastecer {quantidade_litros:.2f} litros de {combustivel}. ", end='')
if (combustivel == 'etanol') and (quantidade_litros  > 30):
    print(f'Ganhou uma troca de óleo gratuita!')

elif (combustivel == 'etanol') and (quantidade_litros  <= 30):
    print(f'Infelizmente não ganhou uma troca de óleo.')

else:
    print(f'Infelizmente não ganhou troca de óleo.')
