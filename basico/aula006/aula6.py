'''
Iniciar com letra, pode conter número, separar _, letra minusculas
'''
nome = 'Arthur Damasio'
idade = 32
altura = 1.78
e_maior = idade > 18
peso = 80
# IMC = peso/ (altura x altura)
#imc = peso // (altura*altura)
imc = peso / altura ** 2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É Maior:', e_maior)

print(idade*altura)


print(nome,'tem ', idade, 'de idade e seu imc é ', imc)
