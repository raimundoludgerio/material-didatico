import random
# podemos transformar isso em uma função para o código ficar mais organizado
# a função seria "gerarTurma"
nomes = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana']
sobrenomes = ['Silva', 'Souza', 'Oliveira', 'Santos', 'Lima', 'Costa', 'Ferreira', 'Almeida', 'Rocha', 'Barbosa']

estudantes = []

for i in range(10):
    estudante = {
        "nome": random.choice(nomes),
        "sobrenome": random.choice(sobrenomes),
        "idade": random.randint(14, 25)
    }
    estudantes.append(estudante)

# Função para retorna um estudante

# Reorganização dos dados

# nova função com busca mais otimizada

print(estudantes)