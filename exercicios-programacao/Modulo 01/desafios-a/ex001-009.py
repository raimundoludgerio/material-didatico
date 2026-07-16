# Exercícios
# ex01: criar variáveis para armazenar seu nome, idade e altura
nome = "Raimundo"
idade = 25
altura = 1.60
print(f"o seu nome é {nome}, sua idade é {idade} e sua altura é {altura}")

# ex02: incrementar um
contador = 0
contador += 1
print(contador)

# ex003: dobro, triplo, raiz
numero = float(input("Digite um numero: "))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1 / 2)

print(f"O numero {numero} tem o dobro {dobro}, o triplo {triplo} e a raiz quadrada {raiz}")

# ex004: área do quadrado
lado = int(input("Digite um lado: "))
area_quadrado = lado ** 2
areaQuadrado = lado * lado
print(f"a area do quadrado de lado {lado} é {area_quadrado}")
print(f"a area do quadrado de lado {lado} é {areaQuadrado}")

# ex005: média aritimética
numero1 = float(input("Digite a primeira nota: "))
numero2 = float(input("Digite a segunda nota: "))
media = (numero1 + numero2) / 2
print(f"A media é {media}")

# ex006: divisão inteira e resto de divisão
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
resto = numero1 % numero2
divisao = numero1 // numero2
print("-"*40)
print(f"O numero {numero1} dividido por {numero2}", end=' ')
print(f"a divisao interia é {divisao}", end=' ')
print(f"e o resto de {resto}")
print("-"*40)

# ex007: Celsius para fahrenheit
graus_c = float(input('Informe a temperatura em graus C: '))
grau_f = graus_c * 1.8 + 32
print(f'A temperatura em graus F: {grau_f}')


# ex008: calculo IMC
altura = float(input("Informe a sua altura: "))
peso = float(input("Informe o peso: "))
imc = peso / (altura * altura)
print(f"Com a altura {altura} e o peso {peso} o seu imc é {imc:.2f}")

# ex009: km percorrido de um carro alugado
km_rodado = float(input("Informe quantos km o carro rodou: "))
quantidade_dias = int(input("Informe quantos dias o carro rodou: "))

preco_pagar = 60 * quantidade_dias + km_rodado * 0.15

print(f"O carro com {km_rodado} por {quantidade_dias} custou um total de R${preco_pagar:.2f}")