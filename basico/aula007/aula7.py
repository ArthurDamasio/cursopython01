nome = 'Arthur Damasio'
idade = 32
altura = 1.78
e_maior = idade > 18
peso = 80
# IMC = peso/ (altura x altura)
#imc = peso // (altura*altura)
imc = peso / altura ** 2

print(nome,'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome,idade,imc))

print('{0} tem {1} anos seu imc é {2:.2f}'.format(nome,idade,imc))

print('{n} tem {i} anos seu imc é {im:.2f}'.format(n=nome,i=idade,im=imc))

