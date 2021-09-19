"""
trocando valor de variarveis
"""

x = 10
y = 'Arthur'

# Trocando de forma tradicional
# z = x
# x = y
# y = z

# print(f'x={x} e y={y}')

# No Python
# print(f'x={x} e y={y}')

# x, y = y, x
# print(f'x={x} e y={y}')

z = 'Damasio'
print(f'x={x} e y={y} e z={z}')

x, y, z = z, x, y
print(f'x={x} e y={y} e z={z}')
