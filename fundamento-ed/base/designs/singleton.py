class DatabaseConnection:
    _instance = None

    def __new__(cls):
        # Sobrescreve __new__ para controlar a criação de instâncias
        if cls._instance is None:
            print("Criando nova conexão com o banco de dados...")
            cls._instance = super().__new__(cls)
            cls._instance.connection_status = "Ativa"
        return cls._instance



db1 = DatabaseConnection()
print(f"Status da conexão 1: {db1.connection_status}")

db2 = DatabaseConnection()
print(f"Status da conexão 2: {db2.connection_status}")
db2.connection_status = "Inativa"  # Altera o status para ambas as referências

print(f"Mesma instância? {db1 is db2}") # True