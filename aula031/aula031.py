"""
Desafio
"""
# 2 contadores
# um progressivo
# outro de regressiva
a = 0
b = 10

while a != 10 and b != 1:
    print(a, b)
    a = a + 1
    b = b - 1

# print(a, b)

print('## Outra forma')

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
