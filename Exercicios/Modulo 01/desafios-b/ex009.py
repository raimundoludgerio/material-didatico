# Q09 - Implementar a média ponderada
# Solução desenvolvida por: Arthur Coutinho da Silva

# Solicitar três notas de um estudante e seus respectivos pesos
nota1 = float(input('Digite a primeira nota: '))
peso1 = int(input('Digite o peso da primeira nota: '))

nota2 = float(input('Digite a segunda nota: '))
peso2 = int(input('Digite o peso da segunda nota: '))

nota3 = float(input('Digite a terceira nota: '))
peso3 = int(input('Digite o peso da terceira nota: '))

# Calcular a média ponderada do aluno
soma_das_multiplicacoes = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)
soma_pesos = peso1 + peso2 + peso3
media_ponderada = soma_das_multiplicacoes / soma_pesos

# Apresentar a média ponderada
print(media_ponderada)

# ============= SEGUNDA SOLUÇÃO ============================
# Desenvolvida por: Nayeli Maria da Silva Bezerra

# Crie um programa que armazene as notas e os pesos em variáveis e calcule a média ponderada de um aluno.\

# Notas e pesos
nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
peso3 = float(input("Digite o peso da terceira nota: "))


# Cálculo da média ponderada
media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

# Exibindo o resultado
print(f"A média ponderada é: {media_ponderada:.2f}")