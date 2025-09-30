# arquivo_shrek = open('D:/repositorios-git/estrutura-de-dados/Exercicios/Modulo 2/arquivos/shrek1.txt', "r", encoding="utf8")

# # arquivo_shrek2 = open('../shrek1.txt')
# linhas = arquivo_shrek.readlines()
# for linha in linhas:
#     print(linha)

# arquivo = open("../aula_segundo_ano_a.txt", "w", encoding="utf8")
# for i in range(5):
#     frase = input("Digite alguma frase: ")
#     arquivo.write(frase + "\n")

# arquivo.close()

while True:
    numero_string = input("Informe um número: ")
    numero_string2 = input("Informe um número: ")
    try:
        numero = int(numero_string)
        numero2 = int(numero_string2)
        operacao = numero / numero2
        print(operacao)
    except Exception as ex:
        print("ALGO DEU ERRADO", ex)
