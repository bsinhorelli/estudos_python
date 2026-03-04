numeros = [4, 7, 10, 3, 8, 15, 2]
pares = []
impares = []

for c in numeros:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)

print(f'Lista pares: {pares}\nLista impares: {impares}')