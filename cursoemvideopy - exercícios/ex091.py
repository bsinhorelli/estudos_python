import random
import time
import operator

dados = {
    'jogador1': random.randint(1, 6),
    'jogador2': random.randint(1, 6),
    'jogador3': random.randint(1, 6),
    'jogador4': random.randint(1, 6)
} 

print('Valores Sorteados: ')
for k, v in dados.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(1)
ranking = list()
print('-='*30)
print(F'{'== RANKING DOS JOGADORES ==':^60}')
ranking = sorted(dados.items(), key=operator.itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'                 {i+1}° lugar: {v[0]} com {v[1]}.')
    