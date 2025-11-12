from time import sleep
try:
    arquivo = open("/run/media/Marcos/Novo volume/repositorios-git/estrutura-de-dados/Exercicios/Modulo 02/arquivos/shrek1.txt")
    lista_frases = arquivo.readlines()
    for frase in lista_frases:
        print(frase)
        sleep(0.5)
except Exception as ex:
    print("Não consegui fazer nada", ex)

