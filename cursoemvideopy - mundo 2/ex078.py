lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Escolha um número para posição {cont}: ')))
   
print(f'Maior valor foi o número {max(lista)} na posição {lista.index(max(lista))} ')
print(f'Menor valor foi o número {min(lista)} na posição {lista.index(min(lista))} ')
