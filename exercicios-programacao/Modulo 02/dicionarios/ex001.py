"""
    Faça um programa onde 4 jogadores joguem um dado e tenha um resultado aleatório. 
    Guarde os resultados em um dicionário. No final coloque esse dicionário em ordem 
    sabendo que o vencedor é o jogador que tirou maior número.
"""
from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
    "Jogador 1": randint(1,6),
    "Jogador 2": randint(1,6),
    "Jogador 3": randint(1,6),
    "Jogador 4": randint(1,6)
}
print("Valores sorteados:")
for jogador, pontuacao in jogadores.items():
    print(f"    O {jogador} tirou {pontuacao} no dado")
    sleep(1)

print("")
print("Resultado final:")
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for posicao, jogador in enumerate(ranking):
    print(f"    Na {posicao + 1}º Posição ficou o {jogador[0]} que tirou {jogador[1]} pontos")
    sleep(1.5)