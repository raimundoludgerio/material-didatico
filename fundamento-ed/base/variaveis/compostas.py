meu_dicionario = {
    "nome": "Maria",
    "idade": 25,
    "cidade": "Recife"
}

print(meu_dicionario["nome"])  # Saída: Maria

len(meu_dicionario)     # Número de pares chave:valor
# Obter valores
meu_dicionario.get("nome")        # → Maria

# Adicionar ou atualizar valores
meu_dicionario["idade"] = 30

# Verificar se uma chave existe
"cidade" in meu_dicionario        # → True

# Remover elementos
meu_dicionario.pop("cidade")      # Remove a chave 'cidade'

# Obter todas as chaves, valores ou itens
meu_dicionario.keys()             # → dict_keys(['nome', 'idade'])
meu_dicionario.values()           # → dict_values(['Maria', 30])
meu_dicionario.items()            # → dict_items([('nome', 'Maria'), ('idade', 30)])

# Limpar todo o dicionário
meu_dicionario.clear()


aluno = {
    "nome": "João",
    "notas": [8.5, 9.0, 7.5],
    "aprovado": True
}

print(aluno["nome"])         # João
print(sum(aluno["notas"]))   # 25.0