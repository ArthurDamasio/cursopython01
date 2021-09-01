'''
* Criar variaveis para nome (str), idade (int)
* altura (float) e peso (float de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-strings (com as chaves)

#Luiz tem 32 anos, 1.8 de altura e pesa 80kg.
#O IMC de Luiz é de 24.69
#Luiz nasceu em 1987
'''
nome = 'Arthur'
idade = 32
altura = 1.8
peso= 80.5
ano = 2019
ano_nas = ano - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg')
print(f'O IMC de {nome} é de {imc:.2f}')
print(f'{nome} nasceu em {ano_nas}')

