import json
import os

import hashlib

from cryptography.fernet import Fernet

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

USERS_FILE = os.path.join(os.path.dirname(__file__), '..', 'database', 'database.json')
chave = Fernet.generate_key()

chave_privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
chave_publica = chave_privada.public_key()


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

    def criptografa_fernet(password) -> bytes:
        print(password)
        cipher = Fernet(chave)
        return cipher.encrypt(password.encode())

    def criptografia_rsa(password):
        pass_cipher = chave_publica.encrypt(
            password.encode(),
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        print("Ciphertext (bytes):", pass_cipher[:30], "...")
        return pass_cipher

    def decifra_rsa(password):
        password = chave_publica.decrypt(
            password,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                         algorithm=hashes.SHA256(),
                         label=None)
        )
        print("Senha normal:", password[:30], "...")
        return password

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

    def gerar_hash_senha(password: str) -> str:
        hash_senha = hashlib.sha256(password.encode()).hexdigest()
        return hash_senha

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

    def cifrar_cifra_cesar(password_cifrado: str, deslocamento: int) -> str:
        resultado = ''

        for char in password_cifrado:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                # Desloca para trás
                resultado += chr((ord(char) - base + deslocamento) % 26 + base)
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
        if User.find_by_email(email) or User.find_by_username(username):
            return None  # Usuário já existe

        print("PASS: " + password)
        new_pass = User.criptografa_fernet(password)
        print(new_pass)
        new_user = User(username, email, str(new_pass))
        print(new_user.to_dict())
        users = User.load_all_users()
        users.append(new_user)
        User.save_all_users(users)
        return new_user
