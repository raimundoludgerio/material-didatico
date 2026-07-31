import json

def buscar_usuario_por_id(usuario_id):
    """Função auxiliar para ler o JSON e buscar o usuário."""
    try:
        with open('database/usuarios.json', 'r', encoding='utf-8') as f:
            dados = json.load(f)
            return dados.get(str(usuario_id)) # Retorna o dicionário do usuário ou None
    except FileNotFoundError:
        print("erro ao abrir o arquivo")
        return None