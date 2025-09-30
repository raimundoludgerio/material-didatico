# Q05 - Conversor de moeadas:
# Solução desenvolvida por: Gabrielly Beatriz da Silva Bendito

# 5. Crie um programa que leia quanto de dinheiro a pessoa tem na carteira, em seguida mostre quantos dólares ela pode comprar. Considere $1= R$5,68; (10 pontos)

# Solicitar o valor em Real:
real = float(input('Digite o valor que há em sua carteira(R$): '))

# Calcular valor em Dólar:
dolar = (real/5.68)

# Exibir o valor da conta bancária:
print(f'O valor da sua conta é R${real}, convertido para Dólar será: ${dolar:.2f}.')