"""
Desenvolva um programa que leia 4 valores do teclado e guarde em uma tupla. No final o programa deve mostrar:
    Quantas vezes apareceu um valor maior que 9;
    Em que posição foi digitado o primeiro valor 3;
    Quais foram os números pares.
"""
tupla_numeros = (
    int(input("Informe o primeiro valor: ")), 
    int(input("Informe o segundo valor: ")), 
    int(input("Informe o terceiro valor: ")), 
    int(input("Informe o quarto valor: "))
)

print("Os valores digitados foram", tupla_numeros)
print(f"O número 9 apareceu {tupla_numeros.count(9)} vezes")
if 3 in tupla_numeros:
    print(f"O número 3 apareceu na {tupla_numeros.index(3) + 1}º posição")
else:
    print("O número 3 não foi digitado")
print("Os valores pares digitados foram: ", end='')
for numero in tupla_numeros:
    if numero % 2 == 0:
        print(numero, end=' ')
print()

