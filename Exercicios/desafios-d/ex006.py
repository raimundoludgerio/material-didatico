"""
    Escreva um programa que solicite o salário de um funcionário e calcule
    o valor do aumento. Para salários maiores que R$2350,00 o aumento é 10%,
    para valores menores o aumento é de 15%.

    Solução desenvolvida por: Ludimilla Mary Duarte Coelho da Silva
"""

# Ler o salário do funcionário
salario = float(input("Digite o salário do funcionário: R$ "))

# Definir as porcentagens de aumento
if salario > 2350.00:
    aumento = salario * 0.10  # 10% de aumento
else:
    aumento = salario * 0.15  # 15% de aumento

# Calcular o novo salário
novo_salario = salario + aumento

# Exibir os resultados
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")