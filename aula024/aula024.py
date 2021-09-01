"""

Emoticon
print("\U0001F917")
print("\U0001F918")
print("\U0001F919")
print("\U0001F920")

For/ Else em Python
"""

var = ['Arthur Damasio', 'Joaozinho', 'Maria']

# comeca_com_j = False
for valor in var:

    if valor.lower().startswith('j'):
        # comeca_com_j = True
        continue
    print(valor)
else:
    print('Não existe uma palavra que começa com J')


#
# if comeca_com_j:
#     print('Existe uma palavra que começa com J')
# else:
#     print('Não existe uma palavra que começa com J')
