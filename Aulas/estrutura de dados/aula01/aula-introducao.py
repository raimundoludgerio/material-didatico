import random
# podemos transformar isso em uma função para o código ficar mais organizado
# a função seria "gerarTurma"
nomes = ['Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana']
sobrenomes = ['Silva', 'Souza', 'Oliveira', 'Santos', 'Lima', 'Costa', 'Ferreira', 'Almeida', 'Rocha', 'Barbosa']

estudantes = []

for i in range(50):
    estudante = {
        "nome": random.choice(nomes),
        "sobrenome": random.choice(sobrenomes),
        "idade": random.randint(14, 25),
        "matricula": random.randint(1000,1500000)
    }
    estudantes.append(estudante)

# Função para retorna um estudante

def escolha_estudante(lista_estudante, matricula):
    encontrado = "Não encontrado"
    for aluno in lista_estudante:
        if aluno["matricula"] == matricula:
            print("Encontreiiii")
            encontrado = aluno
    return encontrado

matricula = estudantes[25]["matricula"]

estudante_encontrado = escolha_estudante(estudantes, 8763387)
print(estudante_encontrado)
# Reorganização dos dados

# nova função com busca mais otimizada
#for estudante in estudantes:
#    print(estudante["nome"], estudante["sobrenome"], estudante["matricula"])