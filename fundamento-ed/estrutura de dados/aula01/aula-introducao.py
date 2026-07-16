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


#print(estudantes)


# Função para retorna um estudante

def escolha_estudante(lista_estudante, nome):
    encontrado = []
    for aluno in lista_estudante:
        if aluno["nome"] == nome:
            print("Encontreiiii")
            encontrado.append(aluno)
    if encontrado == []:
        return "Não encontrado"
    return encontrado

matricula = estudantes[25]["matricula"]

estudante_encontrado = escolha_estudante(estudantes, nome="Richard")
print(estudante_encontrado)
# Reorganização dos dados

# nova função com busca mais otimizada
#for estudante in estudantes:
#    print(estudante["nome"], estudante["sobrenome"], estudante["matricula"])