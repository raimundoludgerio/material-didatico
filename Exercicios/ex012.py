# ex012: Coordenadas de um ângulo
# Resolução feita por Matheus de Almeida Lourenço
from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do ângulo: '))
radianos = radians(angulo)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)

print(f'O seno do ângulo {angulo} é de {seno:.4f}')
print(f'O cosseno do ângulo {angulo} é de {cosseno:.4f} ')
print(f'A tangente do ângulo {angulo} é de {tangente:.4f}')