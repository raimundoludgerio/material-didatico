import copy

class Inimigo:
    def __init__(self, tipo, vida):
        self.tipo = tipo
        self.vida = vida

    def clone(self):
        return copy.deepcopy(self)

# Uso
inimigo_base = Inimigo("Zumbi", 100)
inimigo_clone = inimigo_base.clone()
print(inimigo_clone.tipo)  # Saída: "Zumbi"