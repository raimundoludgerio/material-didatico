# Q6 - Tinta necessária para pintar uma parede
# Solução desenvolvida por: Mynd Lynx Gomes de Morais
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = altura * largura

tinta = area / 2

print(f'Você precisará de {tinta} litros de tinta.')