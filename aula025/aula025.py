"""
Split, Join Enumerate em Python
* Split - Dividir uma string #str
* Join - Junta uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""
# str = "O Brasil é o o o o pais do futebol, o Brasil é penta."
# lista = str.split(' ')
# lista2 = str.split(',')
# print(lista)
# print(lista2)

# palavra = ''
# contagem = 0
# for vl in lista:
#     qtd_vezes = lista.count(vl)
#     # print(f'A palavra {vl} apareceu {lista.count(vl)}x na frase')
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = vl
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')


# for vl in lista2:
#     print(vl.strip().capitalize())

string = 'O Brasil é penta'
lista = string.split(' ')

# string2 = ','.join(lista)
#
# print(string)
# print(lista)
# print(string2)

for indice, v2 in enumerate(lista):
    print(indice,v2, lista[indice])