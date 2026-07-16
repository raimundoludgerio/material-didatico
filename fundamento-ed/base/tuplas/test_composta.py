from aula01b import analisar_texto

frase = input("Informe uma frase: ")
tuple_retorno = analisar_texto(frase)


print(tuple_retorno)



tupla_numeros = ("sim", "não")
lista_nomes = ["Arthur", 3, "Gleycy"]


lista_nomes[1] = "Gessica"
lista_nomes.append("Raimundo")
nome = lista_nomes.pop(2)
nome1 = lista_nomes.remove("Arthur")
del lista_nomes[0]

print(nome)
print(nome1)
print(lista_nomes)