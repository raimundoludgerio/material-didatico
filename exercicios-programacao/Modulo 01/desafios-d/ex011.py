"""
    Elabore um programa que calcule o valor a ser pago por um produto,
    levando em conta o seu preço normal e a condição de pagamento: à vista com
    10% de desconto, à vista no cartão com 5% de desconto, em até 2x no cartão
    com preço normal, e acima de 3x no cartão com juros de 20%.

    Solução desenvolvida pelo professor.
"""


def exibir_menu():
    print("="*40)
    print("Informe uma opção: ")
    print("1: à vista, com 10%".center(40))
              
    print("2: à vista + cartão, com 5% de desconto")
    print("3: Cartão, até 2x, sem desconto: ")
    print("4: Cartão, com mais de duas vezes, com 20% de juros ")
    print("9: Exibir as opções ")
    print("0: Sair ")
    print("="*40)
exibir_menu()
valor_produto = int(input("Informe o valor do produto: "))
opcao = int(input("Informe qual opção: "))
while opcao != 0:
    if opcao == 1:
        valor_final = valor_produto - (valor_produto * 0.10)
    elif opcao == 2:
        valor_final = valor_produto - (valor_produto * 0.05)
    elif opcao == 3:
        valor_final = valor_produto
    elif opcao == 4:
        valor_final = valor_produto + (valor_produto * 0.2)
    elif opcao == 9:
        exibir_menu()
    else:
        print("OPÇÃO INVÁLIDA!")
    print(f"O valor final do \n prduto foi de R${valor_final:.2f}")
    print("O valor \n do produto é:", valor_produto)
    print("a opção esolhida foi {} VALOR DO PODUTO É R${}".format(opcao, valor_produto))


    valor_produto = int(input("Informe o valor do produto: "))
    opcao = int(input("Informe a opção: "))

