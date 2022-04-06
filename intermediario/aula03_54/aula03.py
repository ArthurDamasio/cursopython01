#
# exercícios
#
# 01 ~~~~~~~~~~
def f(saudacao, nome):
    print(saudacao, nome)


f('ola amizade', 'JJ')
f(nome='JJ', saudacao='ola amizade', )


# 02 ~~~~~~~~~~

def f2(num1, num2, num3):
    print(num1 + num2 + num3)


f2(1, 1, 1)


# 03 ~~~~~~~~~~
def f3(num1, num2):
    return num1 + (num1 * (num2 / 100))


print(f3(100, 20))


# 04 ~~~~~~~~~~
def f4(var):
    if var % 5 == 0 and var % 3 == 0:
        return f'FizzBuzz, {var} é div 3 e 5'
    if var % 5 == 0:
        return f'buzz, {var} é div 5'
    if var % 3 == 0:
        return f'fizz, {var} é div 3'
    else:
        return var

from random import randint

for i in range(100):
    aleatorio = randint(0,100)
    print(f4(aleatorio))
