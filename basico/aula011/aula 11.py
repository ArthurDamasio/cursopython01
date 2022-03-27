'''
Operadores Relacionais - Aula 4
== > >= < <= !=
'''
num_1 = 'Luiz'
num_2 = 'Otávio'
expressao = (num_1!=num_2)
print(expressao)

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

# Limite para pegar empréstimo
# idade_limite = 18

idade_menor = 20
idade_maior = 30

if int(idade) >= idade_menor and int(idade) <= idade_maior:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} não pode pegar empréstimo')


