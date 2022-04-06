#
# Funções - def em python
#

def funcao():
    print('python para blockchain')


funcao()
funcao()
funcao()


# ~~~~~~

def funcao02(msg='Opa', home='PRÉDIO'):
    home = home.replace('É', '3')
    msg = msg.replace('O', '0')
    print(msg, home)
    return f'{msg} {home}'


var = funcao02()
print(var)

# funcao02('Suzano 01', 'casa')
# funcao02('Suzano 03', 'ap')
# funcao02(home='AAA', msg='QUE ISSO')
# funcao02()
