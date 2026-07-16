# contador = 10
# while contador > 0:
#     print(contador)
#     contador -= 1  
# print("Decolar!")

# while True:
#     resposta = input("Digite 'sair' para terminar: ")
#     if resposta == 'sair':
#         break
#     else:
#         continue

def calcula_area_perimetro(raio):
    area = 3.14 * raio ** 2
    perimetro = 2 * 3.14 * raio
    return area, perimetro

a, p = calcula_area_perimetro(5)
print(f"Área: {a:.2f}, Perímetro: {p:.2f}")



def lista_compras(*itens):
    print("Compre:")
    for item in itens:
        print(f"- {item}")



lista_compras("maçã", "leite", "pão") 