"""
Crie uma tupla contendo os 20 times que ocupam as posições da tabela do Campeonato Brasileiro de Futebol, organizados por ordem de colocação (do 1º ao 20º). Em seguida, desenvolva um programa que:
    Exiba os 5 primeiros colocados.
    Mostre os 4 últimos colocados da tabela.
    Apresente os times em ordem alfabética.
    Informe a posição do time "Fortaleza" na tabela.

"""

times_brasileirao_2025 = (
    "Atlético Mineiro",
    "Bahia",
    "Botafogo",
    "Ceará",
    "Corinthians",
    "Cruzeiro",
    "Flamengo",
    "Fluminense",
    "Fortaleza",
    "Grêmio",
    "Internacional",
    "Juventude",
    "Mirassol",
    "Palmeiras",
    "Red Bull Bragantino",
    "Santos",
    "São Paulo",
    "Sport",
    "Vasco da Gama",
    "Vitória"
)


print("-="*70)
print("Todos os times do brasileirão:", times_brasileirao_2025)
print("-="*70)
print("Os 5 primeiros do campeonato:", times_brasileirao_2025[:5])
print("-="*70)
print("Os 4 últimos do campeonado:", times_brasileirao_2025[15:])
print("-="*70)
print("Todos os times em ordem", sorted(times_brasileirao_2025))
print("-="*70)
print(f"O Fortaleza está na {times_brasileirao_2025.index("Fortaleza") + 1}º posição")
