senha_secreta = "python123"
tentativa = ""

while tentativa != senha_secreta:
    tentativa = input("Digite a senha: ")
    if tentativa != senha_secreta:
        print("Senha incorreta! Tente novamente.")

print("Acesso permitido! Bem-vindo(a)!")