caixas = ["bala", "pirulito", "chiclete", "doce podre", "bala", "pirulito"]
indice = 0

while indice < len(caixas):
    print(f"Abrindo a caixa {indice}: {caixas[indice]}")

    if caixas[indice] == "doce podre":
        print("Eca! Doce podre! Fim do jogo.")
        break
    indice += 1

print("FIM!")