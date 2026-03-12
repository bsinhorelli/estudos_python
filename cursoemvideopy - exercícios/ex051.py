a1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = a1 + (10 - 1) * razao

for c in range(a1, pa, razao):
    print(c, end=' -> ')
print('ACABOU!!!')