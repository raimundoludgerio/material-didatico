def cabecalho():
    print("="*30)
    print(f'{'Seja Bem Vindo!':^30}')
    print("="*30)

def analisar_texto(texto):
    cont_consoante = 0
    cont_vogal = 0
    cont_espaco = 0
    tupla_vogais = ('a', 'e', 'i', 'o', 'u')
    for letra in texto:
        if str(letra).lower() in tupla_vogais:
            cont_vogal += 1
        elif str(letra).lower() == " ":
            cont_espaco += 1
        else:
            cont_consoante += 1
    return cont_consoante, cont_vogal, cont_espaco
