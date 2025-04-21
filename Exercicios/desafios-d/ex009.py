"""
    A Confederação Nacional de Natação necessita de um programa que leia
    o ano de nascimento de um atleta e exiba a sua categoria de acordo com a
    idade. As categorias são as seguintes: mirim para até 9 anos, infantil até 14
    anos, júnior até 19 anos, sênior até 20 anos e mestre para maiores de 20 anos.

    Solução desenvolvida por: Adrian Barbosa Silva
"""


from datetime import date

# Solicitar o ano de nascimento do atleta
ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))

# Calcular a idade com base no ano atual
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

# Verificar a categoria de acordo com a idade
if idade <= 9:
    categoria = "MIRIM"
elif idade <= 14:
    categoria = "INFANTIL"
elif idade <= 19:
    categoria = "JÚNIOR"
elif idade <= 20:
    categoria = "SÊNIOR"
else:
    categoria = "MESTRE"

# Exibir a categoria
print(f"Idade: {idade} anos")
print(f"Categoria: {categoria}")