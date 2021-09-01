#       Índices
#       0123456789...............................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_user = input('qual letra deseja colocar maiúscula: ')

# Iteração <- Iterar
while contador < tamanho_frase:
    # print(frase[contador], contador)
    letra = frase[contador]
    if letra == input_do_user:
        nova_string += input_do_user.upper()
    else:
        nova_string += letra
    # nova_string += frase[contador]
    # print(nova_string)
    contador += 1

print(nova_string)