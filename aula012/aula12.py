"""
Operadores lógicos - Aula 4
and, or, not
in e not in
"""
# (verdadeiro E verdadeiro) = verdadeiro
# (verdadeiro E Falso) = Falso

# (verdadeiro or verdadeiro) = verdadeiro
# (verdadeiro or Falso) = verdadeiro

"""
a = 2
b = 3

if not b > a:
    print('B é maior do que A')
else:
    print('A é maior do que B')

if not b:
    print('preencher o valor de b')

nome = 'Arthur'

if 'u' in nome:
    print("Existe a letra U dentro do seu nome")

"""

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'arthur'
senha_bd = '123456'

if  usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')
