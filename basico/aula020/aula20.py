'''
while / else - aula 8
contadores
acumuladores
'''
acumulador = 1
contador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('cheguei no else')
print('isso executa')
