# ex013: sorteio de uma lista
# Solução feita por: José Augusto Batista do Nascimento
from random import choice

alunos = ['Cleitin', 'Jubileu', 'Jeremias','Zé']

print(choice(alunos))


# Solução 02: Feita pelo professor
aluno1 = input('Qual o nome do primeiro aluno? ')
aluno2 = input('Qual o nome do segundo aluno? ')
aluno3 = input('Qual o nome do terceiro aluno? ')
aluno4 = input('Qual o nome do quarto aluno? ')

alunos = [aluno1, aluno2, aluno3, aluno4]

aluno_escolhido = choice(alunos)
titulo = "O aluno escolhido foi:"
print("=" * 80)
print(f"{titulo:^80}")
print(f"{aluno_escolhido:^80}")
print("=" * 80)