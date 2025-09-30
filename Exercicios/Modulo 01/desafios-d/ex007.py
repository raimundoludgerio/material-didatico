"""
Para que três segmentos de reta formem um triângulo, a soma de quaisquer dois lados deve ser maior que o terceiro lado.
Considere um triângulo com lados de comprimentos 3, 4 e 5.
3 + 4 > 5 (7 > 5) - ✅
3 + 5 > 4 (8 > 4) - ✅
4 + 5 > 3 (9 > 3) - ✅
Como todas as condições são satisfeitas, esses segmentos formam um triângulo válido.
Enquanto 1, 2 e 4 não formam um triângulo.
1 + 4 > 2 (5 > 2) ✅
2 + 4 > 1 (6 > 1) ✅
1 + 2 > 4 (3 > 4) ❌ (Falso)
Como uma das condições falha (1 + 2 não é maior que 4),
esses três segmentos não podem formar um triângulo.


Desenvolvida por: Adeilma Batista do Nascimento

"""

r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))


if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As retas podem formar um triângulo!")
else:
    print("As retas não podem formar um triângulo.")