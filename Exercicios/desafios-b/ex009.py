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