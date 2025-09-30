"""
    Questão 05: Faça um programa que leia a velocidade de um carro e se a velocidade
    ultrapassar 80km/h, o carro deverá ser multado. O programa deverá informar
    que o carro foi multado e o valor calculado com base em 7 reais para cada km
    excedente a velocidade máxima.

    Solução feita por: Maria de Fátima Pereira da Silva

"""

velocidade = float(input('Insira a velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você foi multado em {multa} reais.')
else:
    print('Dentro do limite de velocidade!')