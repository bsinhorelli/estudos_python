despensa = ['leite', 'arroz','feijao']
item_desejado = str(input('Digite o item que você quer verificar: ')).lower()

if item_desejado not in despensa:
    print(f'O item {item_desejado} precisa ser comprado!')
                
else:
    print(f'O item {item_desejado} ainda está disponivel na despensa.')
