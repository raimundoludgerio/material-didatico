def inserir(nome, lista):
    if lista == None:
        raise ValueError("Erro ao adicionar na lista")
    lista.append(nome)
    return lista

nome = "Raimundo"
try:
    lista = inserir(nome, None)
    print(lista)
except ValueError as erro:
    print(erro)
