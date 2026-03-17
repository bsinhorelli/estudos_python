pessoa = dict()
pessoas = list()
while True:
    pessoa['nome'] = input('Nome: ')
    
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper()
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    while True:
        opcao = input('Quer continuar? [S/N] ').upper()
        if not opcao in 'SN':
            print('ERRO! Digite apenas S ou N.')
        else:
            break
    if opcao == 'N':
        print('-='*30)
        break

print(pessoas)
print(f'Foram cadastradas {len(pessoas)} pessoas.')

