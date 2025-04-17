"""
    Questão 11: Senha de sistema.

   Desenvolvida por: Mynd Lynx Gomes de Morais
"""

# 11. Crie um sistema de login que peça um nome de usuário e senha. Se o usuário for "admin" e a senha for "1234", exiba "Acesso permitido", caso contrário, mostre "Acesso negado".
usuario = input('Nome de usuário: ').lower()
senha = input('Senha: ')

if usuario == 'admin' and senha == '1234':
  print('Acesso permitido.')
else:
  print('Acesso negado.')

