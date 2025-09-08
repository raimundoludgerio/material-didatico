"""
    Questão 09: Alistamento militar

    Desenvolvida por: Mynd Lynx Gomes de Morais
"""

# 9. Crie um programa que solicite o ano de nascimento de um jovem e, com base na idade, informe se ele ainda precisa se alistar, se está no momento do
# alistamento ou se já passou do prazo. O programa também deve exibir quanto tempo falta ou há quanto tempo o alistamento deveria ter ocorrido.

ano = int(input('Digite o seu ano de nascimento: '))
idade = 2025 - ano

if idade < 18:
  print('Você ainda precisa se alistar.')
  tempo = 18 - idade
  print(f'Você deve se alistar em {tempo} ano(s).')
elif idade == 18:
  print('Está no momento de você se alistar!')
else:
  print('O seu alistamento passou do prazo.')
  tempo = idade - 18
  print(f'Você deveria ter se alistado a {tempo} ano(s)')