#
# Funções - def em python
#

# def funcao1(var):
#     return var
#
#
# variavel = funcao1('valor que eu quero')
#
# if variavel:
#     print(variavel)
# else:
#     print('Nenhum valor')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def divisao(n1, n2):
#     if n2 == 0:
#         return
#
#     return n1 / n2
#
# div = divisao(4, 2)
#
# if div:
#     print(div)
# else:
#     print('conta invalida')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def f(var):
#     print(var)
#
#
# def dumb():
#     return f
#
#
# # var = dumb()('E colocar o meu valor aqui.')
#
# var1 = dumb()
# print(id(var1), id(f))
#
# if var1 == f:
#     print('var é igual a f')
# else:
#     print('Blaaaaaa')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dumb():
    return ('Luiz','Otávio')

var=dumb()
print(var[0], type(var))