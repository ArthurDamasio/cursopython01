'''
Lista em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
'''
# l1 = [1, 2, 3]
# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# l3 = l1 + l2
# l1.extend(l2)
# l2.append('b')
# l2.insert(0, 'banana')
# l2.pop()
# print(max(l2))
# print(min(l2))
# del(l2[0])

# l2 = list(range(0,100, 8))


# print(l2)
# soma = 0
# for valor in l2:
#     soma = soma + valor
#     print(soma)

# l2 = ['String', True, 10, -20.5]
# for elem in l2:https://www.udemy.com/staticx/udemy/js/webpack/icon-play.ac3f32ecb72a0c3f674fa5a3f3062a56.svg
#      print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')

secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você Perdeu')
        break
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Uhum, a letra "{letra}" existe na palavra secreta. ')
    else:
        print(f'Aafff, a letra "{letra}" NÃO existe na palavra secreta. ')
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print(f'Que legal, VOCÊ GANHOU!!!!! A palavra era {secreto_temp}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temp}')

    if letra not in secreto:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')
    print()
    # print(digitadas)
