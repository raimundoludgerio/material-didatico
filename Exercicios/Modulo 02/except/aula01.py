try:
    # Tenta fazer a conversão
    var = str("2")
except TipoDaExcecao:
    # Caso dê errado
    print("ops... Algo deu errado :(")
else:
    # Quando não ocorrrer nenhuma exceção (opcaional)
    print("Deu tudo certo, amém.")
finally:
    # Sempre vai executar independente de ter dado ou não a exception
    print("Se der errado ou se deu certo, essa mensagem aparece")

