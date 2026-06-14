import os
import json
from werkzeug.security import generate_password_hash, check_password_hash

DB_FILE = 'database/users.json'

def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, 'r') as file:
        return json.load(file)

def save_users(users):
    with open(DB_FILE, 'w') as file:
        json.dump(users, file, indent=4)

def user_exists(username):
    users = load_users()
    return username in users

def create_user(username, password):
    users = load_users()
    users[username] = {
        'password': generate_password_hash(password)
    }
    save_users(users)

def authenticate_user(username, password):
    users = load_users()
    if username in users and check_password_hash(users[username]['password'], password):
        return True
    return False