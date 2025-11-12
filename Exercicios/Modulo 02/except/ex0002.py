try:
    numero = int(input("Informe um número: "))
    numero2 = int(input("Informe outro número: "))
    operacao = numero / numero2
    arquivo = open("divisao.txt", "a")
    arquivo.write(str(operacao))
    arquivo.close()

except Exception:
    print("Deu erro")
else:
    print("apenas quando o try der certo")
finally:
    print("SEMPRE VAI EXECUTAR")

print("FIM")
