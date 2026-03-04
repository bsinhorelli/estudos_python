def somar_lista(lista):
    soma = 0
    for c in lista:
        soma += c
    return soma
    
numeros = [2, 5, 8, 3]
resultado = somar_lista(numeros)
print(resultado)

