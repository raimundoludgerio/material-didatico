
caminho = ""
modo = "r"

# Abrindo e lendo dados de um arquivo
# arquivo = open("../codigo_da_vinci.txt", "r",encoding='utf-8')
novo_arquivo = open("../novo.txt", "w", encoding='utf-8')
novo_arquivo.write("Faroeste Cabloco")
novo_arquivo.write("\n")
novo_arquivo.write("Não tinha medo o tal João")
frases = []
for i in range(5):
    frase = input("Informe uma frase: ")
    frases.append(frase+"\n")
novo_arquivo.writelines(frases)
# linhas = arquivo.readlines()
# for linha in linhas:
#     print(linha)
# print(linhas)
novo_arquivo.close()

# # Abrindo e lendo todas as linhas de um arquivo
# arquivo = open("Exercicios/Modulo 2/arquivos/dados.txt", "r")
# todas_as_linhas = arquivo.readlines()
# print(todas_as_linhas)
# arquivo.close()





# with open("dados.txt", 'w') as arquivo:
#     arquivo.write("Raimundo")


# lista_strings = ["Raimundo", "Marcos", "Professor"]
# with open("dados_professor.txt", 'w') as arquivo:
#     arquivo.writelines(lista_strings)



# with open('Exercicios/Modulo 2/arquivos/codigo_da_vinci.txt', 'r') as codigo_da_vinci:
#     todas_as_linhas = codigo_da_vinci.readlines()
#     for linha in todas_as_linhas:
#         print(linha)
    