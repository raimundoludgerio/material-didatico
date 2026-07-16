from random import randint
print('=' * 40)
print("Vamos brincar de par ou ímpar?".center(40))
print('=' * 40)
tentativas = 0
while True:
    jogador = int(input("Escolha um número: "))
    maquina = randint(1, 10)
    escolha = str(input("Você deseja par ou ímpar [P|I]: ")).lower()
    soma = maquina + jogador
    resultado = 'par' if soma % 2 == 0 else 'ímpar'
    venceu = (escolha == 'p' and resultado == 'par') or (escolha == 'i' and resultado == 'ímpar')
    print("-"*80)
    print(f"Você jogou {jogador} e a máquina {maquina}. Total: {soma} -> {resultado.upper()}")
    print("-"*80)
    if venceu:
        print("🎉 Você venceu essa rodada! Vamos de novo!")
        tentativas += 1
    else:
        print(f"😢 Você perdeu! Total de vitórias consecutivas: {tentativas}")
        break
