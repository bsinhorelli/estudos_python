def maior_menor(lista):
    maior = lista[0]
    menor = lista[0]
    
    for c in lista:
        if c > maior:
            maior = c
        else:
            menor = c
    return maior, menor

numeros = [12, 5, 8, 21, 3]

maior, menor = maior_menor(numeros)
print(f'maior: {maior}')
print(f'menor: {menor}')