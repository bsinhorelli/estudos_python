lista = ['Ana', 'Bruno', 'Joao', 'Pedro']
convidado = input('Digite o nome do convidado que deseja adicionar: ')
posicao = int(input('Digite a posição que deseja adicionar: '))
lista.insert(posicao - 1, convidado)
print(f'Lista Atualizada: {lista}')