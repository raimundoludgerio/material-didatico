nome = str(input('Digite seu nome: ')).capitalize()
print(nome)
if nome == "Raimundo":
    print("Seu nome é muito bonito!!")
elif nome == "Julia" or nome == "Pedro" or nome == "João":
    print("Esse é um belo nome!")
elif nome in "Sousa Socorro Andrade Santos":
    print("Seu nome é bem comum")
elif "Raimundo" in nome:
    print("Seu nome é muito legal")
else:
    print("Nome normal")
