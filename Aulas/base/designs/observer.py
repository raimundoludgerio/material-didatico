from abc import ABC, abstractmethod

# Interface Observer
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# Interface Subject (Observable)
class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)


# Sujeito Concreto (Fonte de dados meteorológicos)
class EstacaoMeteorologica(Subject):
    def __init__(self):
        super().__init__()
        self._temperatura = 0
        self._umidade = 0

    def set_medicoes(self, temperatura: float, umidade: float):
        self._temperatura = temperatura
        self._umidade = umidade
        self.notify(f"Temperatura: {temperatura}°C, Umidade: {umidade}%")

# Observadores Concretos
class DisplayCelular(Observer):
    def update(self, message: str):
        print(f"[CELULAR] Nova atualização: {message}")

class DisplayTV(Observer):
    def update(self, message: str):
        print(f"[TV] ALERTA METEOROLÓGICO: {message}")

class ServidorWeb(Observer):
    def update(self, message: str):
        print(f"[SERVIDOR] Registrando no banco de dados: {message}")

estacao = EstacaoMeteorologica()
celular = DisplayCelular()
tv = DisplayTV()
servidor = ServidorWeb()

# Registrando observadores
estacao.attach(celular)
estacao.attach(tv)
estacao.attach(servidor)

# Simulando mudança de estado
print("=== Primeira Medição ===")
estacao.set_medicoes(25.5, 60)

# Removendo um observador
estacao.detach(tv)

print("\n=== Segunda Medição ===")
estacao.set_medicoes(28.3, 55)