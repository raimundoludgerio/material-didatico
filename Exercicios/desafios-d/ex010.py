"""
    Atualizei o programa de cálculo de IMC. Agora, o programa deve
    informar se a pessoa está abaixo do peso ideal, com sobrepeso, obesidade ou
    obesidade mórbida.

    Solução desenvolvida por: Kleberson Machado Valentim

"""
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso / (altura ** 2)
print(f"IMC: {imc:.2f}")
resultado = "Abaixo do peso" \
    if imc <= 18.5 else "" or "Peso ideal" \
    if imc <= 25 else "" or "Sobrepeso" \
    if imc <= 30 else "" or "Obesidade" \
    if imc <= 40 else "Obesidade mórbida"
print(resultado)
