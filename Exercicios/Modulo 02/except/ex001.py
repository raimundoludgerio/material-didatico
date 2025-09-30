def le_numero():
    entrada = input("Digite um número inteiro: ")
    try:
        valor = int(entrada)  # aqui pode ocorrer ValueError
    except ValueError:
        print("Você não digitou um número inteiro válido!")
        return None
    else:
        print(f"Você digitou o número {valor}.")
        return valor
# num = le_numero()
# if num is not None:
#     print("Agora vou dividir 100 por esse número.")
#     try:
#         resultado = 100 / num  # aqui pode ocorrer ZeroDivisionError
#     except ZeroDivisionError:
#         print("Erro: divisão por zero não é permitida!")
#     else:
#         print("Resultado:", resultado)
# try:
#     arquivo_shrek = open("../arquivos/shrek1.txt", "r")
# except FileNotFoundError:
#     print("Erro ao ler o arquivo.")


# numeros_pares = []
# numero = int(input("Informe um número par: "))
# if numero %2 != 0:
#     raise ValueError("Por favor, informe um número que seja par")
# numeros_pares.append(numero)
# print(numeros_pares)
# try: 
#     numero1 = int(input("infore um número inteiro positivo: "))
#     numero2 = int(input("infore um número inteiro positivo: "))
#     divisao = numero1 / numero2
#     arquivo_resultado = open("resultado.txt", 'w')
#     arquivo_resultado.write(divisao)
#     arquivo_resultado.close()
# except ValueError:
#     print("O valor informado é inválido, tente novamente")
# except ZeroDivisionError:
#     print("Não é possível efetuar divisão por zero!")
# except IOError:
#     print("Erro ao abrir arquivo!")
# except Exception as ex:
#     print("Algum outro erro aconteceu", ex)


try:
    arquivo_shrek = open("../arquivos/shrek1.txt", 'r')
    historia_completa = arquivo_shrek.readlines()
    for linha in historia_completa:
        print(linha)
except IOError:
    print("Erro ao abrir o arquivo")
else:
    print("Arquivo lido com sucesso!")
finally:
    arquivo_shrek.close()







