
caminho = ""
modo = "r"

# Abrindo e escrevendo em um arquivo
arquivo = open("dados.txt", "w")
arquivo.write("peso: "+str(50))
arquivo.close()


with open("dados.txt", 'w') as arquivo:
    arquivo.write("Raimundo")



