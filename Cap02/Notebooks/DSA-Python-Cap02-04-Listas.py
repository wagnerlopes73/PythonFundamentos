# Listas

# Criando uma lista
listadomercado = ['ovos','farinha','leite','requeijao']
print(listadomercado)
a = listadomercado[0]
print(a)

# Criando lista com diferentes  e atribuindo uma variável
lista3 = [10, 120, "carne"]
item1 = lista3[0]
item2 = lista3[1]
item3 = lista3[2]
print(item1)
print(item2)
print(item3)
print ('\r')

# Substitui string "carne" por "queijo"
lista3[2] = "queijo"
item3 = lista3[2]
print(item3)
print(lista3)


# Listas Aninhadas
familia = [['Wagner','Monica','Vanessa'],['Isabel','Joao','Ana Clara']]
print(familia)

adultos = familia[0]
print(adultos)

filhos = familia[1]
print(filhos)
print(adultos[0], "é pai de",filhos[0],",",filhos[1],"e",filhos[2])


# Linhas aninhadas funcionando como matrizes
listas = [[1,2,3],[4,5,6],[7,8,9]]
print(listas)

numero1 = listas[0][1]
print(numero1)

numero2 = listas[2][2]
print(numero2)


# Concatenar listas
lista_s1 = [1,2,3]
lista_s2 = [11,12,13]
lista_total  = lista_s1 + lista_s2
print(lista_total)
# Verificar se valor está na lista
print(10 in lista_total)
print(11 in lista_total)
# tamanho da lista
print(len(lista_total))
# inserir um valor na lista
lista_total.append(14)
print(lista_total)

# Copia de valores entre listas
old_list = [5,6,7]
new_list = []
for item in old_list:
    new_list.append(item)
print(new_list) # adiciona vários valores a lista

new_list.extend([8,9,10])
print(new_list)
# inserir um valor antes de um determinado indice
new_list.insert(2,"Olá")
print(new_list)