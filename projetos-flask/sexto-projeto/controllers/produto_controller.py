from models.produto import Produto
import json
def get_produtos():
    with open("database/produtos.json", "r") as arquivo:
       return json.load(arquivo)
    

def cadastrar_produto(nome, descricao, preco):
    produtos = get_produtos()
    print(produtos)
    produto = Produto(nome, descricao, preco)
    produto_dict = dict(produto)
    produtos.append(produto_dict)
    
    with open("database/produtos.json", "w") as arquivo:
       json.dump(produtos, f, indent=4)

