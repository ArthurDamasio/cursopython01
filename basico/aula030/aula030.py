"""
operador or
"""

# nome = input('Qual o seu nome? ')

### De forma tradicional
# if nome:
#     print(nome)
# else:
#     print('Voce nao digitou nada =/')

### OR
# print(nome or None or False or 0 or 'Você não digitou nada!')

## exemplo 2
a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Arthur'

var = a or b or c or d or e or f or g

print(var)
