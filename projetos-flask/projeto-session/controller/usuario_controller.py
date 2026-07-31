from models import usuario
def recuperar_usuario(id):
    if id is not None:
        return usuario.buscar_usuario_por_id(id)
    return None


def valida_login(login, senha):
    usuario_logado = usuario.buscar_usuario_por_id(login)
    if usuario_logado: # Usuário foi encontrado
        return usuario_logado["senha"] == senha # se senhas forem iguais, retorna True
    return False