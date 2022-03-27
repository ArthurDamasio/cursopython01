'''
Faça um prog que peça ao usuario para dig um num int,
informe se este num é par ou impar. Caso o usuario não digite um num inteiro,
informe que não é um numero inteiro
'''

num1 = input('Digite um numero inteiro: ')

try:
    if int(num1) % 2 == 0:
        print(f'o numero {num1} é par')
    else:
        print(f'o numero {num1} é impar')
except:
    print('Por favor informe um numero inteiro')

