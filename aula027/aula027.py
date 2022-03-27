"""
Desempacotamento de listas
"""

lista = ['Luiz', 'maria', 'joao', 1, 2, 3, 4, 5, 6, 7]

n1, n2, *outra_lista, ultimo_da_lista = lista

print(n1, n2, ultimo_da_lista)

print(outra_lista)

n01, n02, *_ = lista

print(_)
