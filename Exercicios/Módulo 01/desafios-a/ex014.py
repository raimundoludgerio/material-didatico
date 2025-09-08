# ex014: sorteio de ordem de alunos
# Solução feita por: Ana Alice Lopes Alves
from random import shuffle

alunos = input("Digite o nome dos alunos: ").split(",")

l_alunos = [aluno.strip() for aluno in alunos]

shuffle(l_alunos)

print(l_alunos)

# Solução alternativa desenvolvida pelo professor

aluno1 = input('Qual o nome do primeiro aluno? ')
aluno2 = input('Qual o nome do segundo aluno? ')
aluno3 = input('Qual o nome do tereceiro aluno? ')
aluno4 = input('Qual o nome do quarto aluno? ')

alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print("=" * 40)
print("A ordem para apagar o quadro é:")
print(f"1º {alunos[0]}")
print(f"2º {alunos[1]}")
print(f"3º {alunos[2]}")
print(f"4º {alunos[3]}")
print("=" * 40)