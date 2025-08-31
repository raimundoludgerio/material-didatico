def analisar_texto(texto):
    cont_consoante = 0
    cont_vogais = 0
    cont_espaco = 0
    tupla_vogais = ("a", "e", "i", "o", "u")
    for letra in texto:
        if letra.lower() in tupla_vogais:
            cont_vogais += 1
        elif letra == " ": 
            cont_espaco += 1
        else:
            cont_consoante += 1
    return (cont_vogais, cont_consoante, cont_espaco)

