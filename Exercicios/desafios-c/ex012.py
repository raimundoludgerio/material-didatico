"""
    Questão 12: Conversão de temperatura.

    Desenvolvida por: Mynd Lynx Gomes de Morais
"""

# 12. Peça ao usuário para escolher entre converter de Celsius para Fahrenheit ou Fahrenheit para Celsius. Em seguida, solicite a temperatura e realize a conversão usando as fórmulas.
escala = input('Escolha a conversão: (1) Celsius para fahrenheit/ (2) Fahrenheit para Celsius: ')
temperatura = int(input('Digite a temperatura: '))

if escala == '1':
  print(f'{(temperatura*9/5)+ 32}°F')
else:
  print(f'{5/9 * (temperatura-32)}°C')