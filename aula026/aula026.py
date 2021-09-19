"""
* Enumerate - Enumerar elementos da lista #list
"""
lista = [
    ['maria','luiz','fernando'],
    ['maria2','luiz2','fernando2'],
    ['maria3','luiz3','fernando3'],
]

# # print(lista[1][2])
#
# enumerada = list(enumerate(lista))
#
# # print(list(enumerada))
#
# print(enumerada[1][1][2])

for v1 in enumerate(lista, 43):
    valor_enumerado, minha_lista = v1
    # print(minha_lista)
    nome1,nome2,nome3 = minha_lista
    print(nome1,nome2, nome3)
