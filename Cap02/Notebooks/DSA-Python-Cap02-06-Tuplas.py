# imutabilidade

# Criando uma tupla
t1 = ("Geografia", 23, "Elefantes")
print(t1)
# tupla1.append("Chocolate") Tupla não permite append pois é imutável
# podem ter apenas 1 item

# para alterar uma tupla deve-se primeira transforná-la em lista, alterá-la e voltar a tupla
lista_t1 = list(t1)
print(lista_t1)
lista_t1.append(40)
print(lista_t1)
t1 = tuple(lista_t1)
print(t1)
