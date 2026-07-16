senha_secreta = "python123"
tentativa = input("Digite a senha: ")

while tentativa != senha_secreta:
    if tentativa != senha_secreta:
        print("Senha incorreta! Tente novamente.")
    tentativa = input("Digite a senha: ")

print("Acesso permitido! Bem-vindo(a)!")