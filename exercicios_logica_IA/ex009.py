def separar_pares_impares(lista):
    pares = []
    impares = []
    for c in lista:
        if c % 2 == 0:
            pares.append(c)
        else:
            impares.append(c)
    return pares, impares

numeros = [1, 2, 3, 4, 5, 6, 7]

pares, impares = separar_pares_impares(numeros)
print(pares) 
print(impares)   