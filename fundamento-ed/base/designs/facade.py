class Amplificador:
    def ligar(self):
        print("Amplificador ligado")

    def configurar_audio(self):
        print("Audio configurado (5.1 surround)")

    def set_volume(self, nivel):
        print(f"Volume ajustado para {nivel}")


class Projetor:
    def ligar(self):
        print("Projetor ligado")

    def modo_widescreen(self):
        print("Modo widescreen ativado")

    def desligar(self):
        print("Projetor desligado")


class Luzes:
    def atenuar(self, nivel):
        print(f"Luzes atenuadas para {nivel}%")


class HomeTheaterFacade:
    def __init__(self):
        self.amp = Amplificador()
        self.proj = Projetor()
        self.luzes = Luzes()

    def assistir_filme(self, filme):
        print("\nIniciando modo cinema...")
        self.luzes.atenuar(10)
        self.amp.ligar()
        self.amp.configurar_audio()
        self.amp.set_volume(70)
        self.proj.ligar()
        self.proj.modo_widescreen()
        self.player.ligar()
        self.player.play(filme)

    def desligar_tudo(self):
        print("\nDesligando sistema...")
        self.proj.desligar()
        self.amp.set_volume(0)
        # ... outros desligamentos

# Sem Facade (complexo)
amp = Amplificador()
proj = Projetor()
# ... muitas linhas de configuração


# Com Facade (simples)
home_theater = HomeTheaterFacade()
home_theater.assistir_filme("O Poderoso Chefão")