"""
Split, Join Enumerate em Python
* Split - Dividir uma string #str
* Join - Junta uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""
str = "O Brasil é o pais do futebol, o Brasil é penta."
lista = str.split(' ')
lista2 = str.split(',')
print(lista)
print(lista2)

for vl in lista:
    print(vl)
