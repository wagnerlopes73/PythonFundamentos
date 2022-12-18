# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
ex1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ex1)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
ex2 = ["lápis", "caneta", "borracha", "régua", "caderno"]
print(ex2)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
string1 = "Ary "
string2 = "Wagner"
string_final = string1 + string2
print(string_final)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tupla1 = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla1.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dic1 = {}
print(dic1)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dict2 = {"Wagner":49, "Ana Clara":14, "João":14}
print(dict2)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dict2["Isabel"] = 14
print(dict2)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos.
# Imprima o dicionário na tela.
dict3 = {"Wagner":50, "Ana Clara":14, "Filhos":[14,14]}
print(dict3)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string,
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
lista2 = ["Wagner", (20, 30), {"Isabel":14,"João":14}, 3.83]
print(lista2)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
f = frase[0:18]
print(f)
