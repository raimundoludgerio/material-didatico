produtos = {
    "caneta": {"preco": 2.50, "estoque": 120},
    "caderno": {"preco": 15.00, "estoque": 60},
    "borracha": {"preco": 1.00, "estoque": 0}
}

for nome, info in produtos.items():
    if info["estoque"] > 0:
        print(f"{nome.title()} disponível por R$ {info['preco']:.2f}")
    else:
        print(f"{nome.title()} está fora de estoque.")




dias_semana = ("Segunda", "Quarta", "Sexta")
dias_semana[1] = "Terça"
print(dias_semana)




print(qualquer_coisa(10, 7, 5, 8, 9))

