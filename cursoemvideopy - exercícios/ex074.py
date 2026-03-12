import random

numeros = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)

print('Os números sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=(' '))

print(f'\nO maior valor dos números sorteados é: {max(numeros)}')
print(f'O menor valor dos números sorteados é: {min(numeros)}')
