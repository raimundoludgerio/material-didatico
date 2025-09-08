# Q07 - Valor do produto com desconto
# Solução desenvolvida por: Ana Beatriz Ferreira
valor_produto = float(input('Digite o valor do produto: '))

porcentagem = (valor_produto * 5/100)
desconto = (valor_produto - porcentagem)

print(f'O valor do produto é {valor_produto} e com 5% de desconto ficará {desconto}')