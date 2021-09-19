"""
Operador ternário
"""

logged_user = False

# opcao longa
# if logged_user:
#     msg = 'Usuário logado'
# else:
#     msg = 'Usuário precisa logar'

# operacao ternario

# msg = 'Usuário logado' if logged_user else 'Usuário precisa logar'
# print(msg)

idade = input('Qual é sua idade: ')
if not idade.isnumeric():
    print('Voce precisa colocar número')
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar' if e_de_maior else 'Não pode acessar'


