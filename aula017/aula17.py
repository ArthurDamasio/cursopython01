"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 1
print(f'{num1:0>10}')
print(f'{num1:0^11}')

num2 = 1150
print(f'{num2:0>10.2f}')

nome = 'Arthur Damasio'
#print(f'{nome:@>50}')
print(nome.rjust(20,"#"))
print(nome.lower())
print(nome.upper())
print(nome.title())