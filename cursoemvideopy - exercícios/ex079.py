lista = []

while True:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print(f'Número {num} adicionado!')
        
    else:
        print('você já adicionou esse número')
    
    escolha = input('Quer continuar? [S/N] ')
    if escolha.lower() == 'n':
        print('Programa encerrado...')
        break
print('-='*30)
print(f'Números adicionados: {sorted(lista)}')
    