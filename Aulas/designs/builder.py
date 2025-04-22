class Pizza:
    def __init__(self):
        self.ingredientes = []

    def add_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def add_queijo(self):
        self.pizza.add_ingrediente("Queijo")
        return self

    def add_tomate(self):
        self.pizza.add_ingrediente("Tomate")
        return self

    def build(self):
        return self.pizza

# Uso
pizza = PizzaBuilder().add_queijo().add_tomate().build()
print(pizza.ingredientes)  # Saída: ['Queijo', 'Tomate']