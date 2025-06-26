import json
import os

CAMINHO_DB = "database/usuarios.json"

def carregar_usuarios():
    if not os.path.exists(CAMINHO_DB):
        return []
    with open(CAMINHO_DB, 'r', encoding='utf-8') as f:
        return json.load(f)

def autenticar_usuario(login, senha):
    usuarios = carregar_usuarios() # Retonar lista usuários
    
    for u in usuarios:
        print(u)
        if u['login'] == login and u['senha'] == senha:
            return True
    return False