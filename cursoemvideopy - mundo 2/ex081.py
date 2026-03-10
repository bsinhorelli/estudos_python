lista = []
soma = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    
    opcao = input('Quer continuar? [S/N] ')
    if opcao.lower() == 'n':
        print('Programa encerrando...')
        break

for c in lista:
    soma += 1   
print('-='*30)
print(f'Você digitou {soma} valores.')
print(f'Os valores em ordem descresente são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não faz parte da lista.')
       