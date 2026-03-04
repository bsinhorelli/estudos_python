def contar_maiores(lista, valor):
    contador = 0
    for c in lista:
        if c > valor:
            contador += 1
    return contador
    
numeros = [4, 15, 7, 20, 9]
valor = 10

resultado = contar_maiores(numeros, valor)
print(f'{resultado} são maiores do que {valor}')