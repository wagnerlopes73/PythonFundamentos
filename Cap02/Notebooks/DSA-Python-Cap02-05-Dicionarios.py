# Isso é uma lista
estudantes_1st = ["Mateus", 24, "Fernanda", 22, "Tamires", 26, "Cristiano", 25]
print(estudantes_1st)

# Isso é um dicionário
estudantes_dict = {"Mateus":24, "Fernanda":22, "Tamires":26, "Cristiano":25}
print(estudantes_dict)

# retorna o valor do indice pela chave
print(estudantes_dict["Mateus"])

# adiciona um novo rótulo/chave com valor
estudantes_dict["Pedro"] = 40

print(estudantes_dict)

# Limpa o dicionário
estudantes_dict.clear()
print(estudantes_dict)

estudantes_dict = {"Mateus":24, "Fernanda":22, "Tamires":26, "Cristiano":25}

# tamanho dicionário
print(len(estudantes_dict))

# valores das chaves
print(estudantes_dict.values())

# chaves da dicionário
print(estudantes_dict.keys())

# itens da dicionário
print(estudantes_dict.items())

# cria novo dicionário
estudantes2_dict = {"Wagner":49, "João":14, "Ana Clara":14, "Isabel":14}
print(estudantes2_dict)
estudantes2_dict["Wagner"] = 50
print(estudantes2_dict["Wagner"])

# Atualiza o dicionário 1 com dados do dicionário 2 - Tipo concatenar
estudantes_dict.update(estudantes2_dict)
print(estudantes_dict)


# Cria um dicionário vazio
dic1 ={}
#adiciona chave e valor
dic1["key_one"] = 1
#adiciona chave como número e valor como string
dic1[8.2] = "Python"
print(dic1)

# Dicionário de Listas
dict3 = {"key1":1230, "key2":[22,453,73.4], "key3":["leite", "maçã", "batata"]}
print(dict3)
# Acessando um item da lista, dentro do dicionário
a = dict3["key3"][0].upper()
print(a)

# Operações com itens da lista, dentro do dicionário
b = dict3["key2"][1] - 100
print(b)

# Duas operações no mesmo comando, para atualizar um item dentro da lista
dict3["key2"][0] -= 2
c = dict3["key2"][0]
print(c)

