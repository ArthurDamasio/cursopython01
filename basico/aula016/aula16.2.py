'''
faca um programa que perg a hora e baseando-se no horario descrito, exiba a saudação apropriada.
bom dia 0-11
boa tarde 12-17
boa noite 18-23
'''

num1 = input('Digite a hora entre 0 e 23 horas: ')

try:
    if int(num1) >= 0 and int(num1) <= 11 :
        print(f'Bom dia, agora são {num1} horas')
    elif int(num1) >= 12 and int(num1) <= 17 :
        print(f'Boa tarde, agora são {num1} horas')
    elif int(num1) >= 18 and int(num1) <= 23 :
        print(f'Boa noite, agora são {num1} horas')
    else:
        print('Por favor informe a hora entre 00 e 23')
except:
    print('Por favor informe a hora entre 00 e 23')

