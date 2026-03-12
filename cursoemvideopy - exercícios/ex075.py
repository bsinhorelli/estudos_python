valores = int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: '))

print(f'a) O valor 9 apareceu {valores.count(9)} vezes.')

if 3 in valores:
    print(f'b) O valor 3 apareceu na {valores.index(3)}ª posição.')
else:
    print(f'b) O valor 3 não foi encontrado.')

print('Os valores pares encontrados foram: ', end='')
for i in valores:
    if i % 2 == 0:
        print(i, end=' ')

