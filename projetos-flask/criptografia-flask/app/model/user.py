import json
import os
from ctypes import c_int

from cryptography.fernet import Fernet
USERS_FILE = os.path.join(os.path.dirname(__file__), '..', 'database', 'database.json')
chave = Fernet.generate_key()
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'password   ': self.password
        }

    def criptografa_fernet(self) -> bytes:
        cipher = Fernet(chave)
        return cipher.encrypt(self.password.encode())

    def decript_fernet(self) -> str:
        cipher = Fernet(chave)
        return cipher.decrypt(self.password).decode('utf-8')

    def password_descifra(password: str, des: int) -> str:
        result = ""
        for char in password:
            if char.isalpha():
                codigo_base = ord('a') if char.islower() else ord('A')
                codigo_cifrado = (ord(char) - codigo_base - des) % 26 + codigo_base
                result += chr(codigo_cifrado)
            else:
                result += char
        return result

    def decifrar_cifra_cesar(password_cifrado: str, deslocamento: int) -> str:
        resultado = ''

        for char in password_cifrado:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                # Desloca para trás
                resultado += chr((ord(char) - base - deslocamento) % 26 + base)
            else:
                resultado += char  # mantém espaços, números, pontuação
        return resultado

    @staticmethod
    def load_all_users():
        if not os.path.exists(USERS_FILE):
            return []

        with open(USERS_FILE, 'r') as f:
            try:
                users_data = json.load(f)
                return [User(**u) for u in users_data]
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save_all_users(users):
        with open(USERS_FILE, 'w') as f:
            json.dump([u.to_dict() for u in users], f, indent=4)

    @staticmethod
    def find_by_email(email):
        users = User.load_all_users()
        for user in users:
            if user.email == email:
                return user
        return None

    @staticmethod
    def find_by_username(username):
        users = User.load_all_users()
        for user in users:
            if user.username == username:
                return user
        return None

    @staticmethod
    def create_user(username, email, password):
        print("PASS: " + password)
        if User.find_by_email(email) or User.find_by_username(username):
            return None  # Usuário já existe

        new_pass = User.passowrd_transforma(password, 3)
        new_user = User(username, email, new_pass)

        users = User.load_all_users()
        users.append(new_user)
        User.save_all_users(users)
        return new_user