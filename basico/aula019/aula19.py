'''
while em Python - aula 7
utilizando para realizar ações enquanto
uma condição for verdadeira

Requisitos: entender condições e operadores
'''

# x = 0
# while x < 10:
#    if x == 3:
#        x = x + 1
#        continue  # Pulando o x =3
#        # "break" pulando
#
#    print(x)
#    x = x + 1
#
# print('Acabou!')

# x = 0
# y = 0
#
# while x < 10:
#     y = 0
#     while y < 5:
#         # print(f'X vale {x} e Y vale {y}')
#         print(f'({x},{y})')
#         y +=1
#
#     x += 1
#
#
# print('Acabou')

while True:
    print()
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')


    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)

    sair = input('Deseja sair? [s]im [n]ão ')

    if sair == 's':
        break