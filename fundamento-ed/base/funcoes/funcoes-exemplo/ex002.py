def aula_lega(*valores):
    print("Essa aula é chataaaaaa")
    return sum(valores) / len(valores)




meu_dic = {
    'nome': 'Julia',
    'nota':100,
    'matricula': 123456
}

print(meu_dic.items())
meu_dic["nome"] = "Raimundo"
meu_dic["turma"] = "2º B"

for i in meu_dic.items():
    print(f"{i[0]} - {i[1]}")



# print(meu_dic.pop("turma"))
print(meu_dic.values())
print(meu_dic.keys())