dados = dict()
dados['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas o {dados['nome']} jogou? '))
lista = []

for quant in range(0, partidas):
    lista.append(int(input(f'Quantos gols na partida {quant}? ')))
dados['gols'] = lista
dados['total'] = sum(lista)
print('-='*30)
print(dados)
print('-='*30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {dados['nome']} jogou {partidas} partidas.')

for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i}, fez {v} gols. ')
print(f'Foi um total de {dados['total']} gols.')