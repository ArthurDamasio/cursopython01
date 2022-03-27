'''
Faca um programa que peça o primeiro nome do usuario. Se o nome tiver
4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é nomral"; maior que 6 escreva "Seu nome é muito grande".
'''

nom = input('Digite seu primeiro nome: ')

try:
    if len(nom) <= 4:
        print(f'{nom}, seu nome é curto')
    elif len(nom) <= 6:
        print(f'{nom}, seu nome é normal')
    elif len(nom) > 6:
        print(f'{nom}, seu nome é muito grande')
    else:
        print('Por favor digite um nome válido')
except:
    print('Por favor digite um nome válido')

