import json
import os

DATA_FILE = "database/produtos.json" 

def carregar_produtos():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_produtos(usuarios):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4)


def salvar_produto(nome_produto):
    produtos = carregar_produtos()
    novo_produto = {"nome": nome_produto}
    produtos.append(novo_produto)
    salvar_produtos(produtos)
    