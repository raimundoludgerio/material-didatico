import json
class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha_hash = self._gerar_hash(senha)

    def _gerar_hash(self, senha):
        """Gera um hash SHA-256 da senha"""
        return hashlib.sha256(senha.encode('utf-8')).hexdigest()

    def verificar_senha(self, senha):
        """Verifica se a senha fornecida corresponde ao hash armazenado"""
        return self.senha_hash == self._gerar_hash(senha)

    def alterar_senha(self, nova_senha):
        """Altera a senha do usuário"""
        self.senha_hash = self._gerar_hash(nova_senha)

    def __repr__(self):
        return f"<Usuario(login='{self.login}')>"
    
    def encontrar_usuario(self, user):
        arquivo_json = open('dao/user.json', 'r')
        usuarios = json.load(arquivo_json)
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.login == user.login:
                usuario_encontrado = usuario
        return usuario_encontrado