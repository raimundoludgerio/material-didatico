"""
    Faça um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, 
    do zero até o vinte. Faça um programa que leia um número inteiro e mostre esse número por extenso. 
    Caso o usuário informe um número que não esteja entre o intervalo permitido, o programa deve solicitar 
    novamente ao usuário um número que seja válido.
"""


numeros_por_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
)

while True:
    numero = int(input("Informe um número: "))
    if numero < 0 or numero > 20:
        if numero == -1:
            print("Encerrando o programa")
            break
        print("Opção Inválida")
        continue
    print(f"Seu número por extenso é {numeros_por_extenso[numero]}")