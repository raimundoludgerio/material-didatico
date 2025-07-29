from models.produto import Produto

def get_produtos():
    with open("database/produtos.json", "r") as arquivo:
       produtos = arquivo.readlines()
    return produtos    

def cadastrar_produto(nome, descricao, preco):
    produto = Produto(nome, descricao, preco)
    with open("database/produtos.json", "w") as arquivo:
       arquivo.writelines(produto)

