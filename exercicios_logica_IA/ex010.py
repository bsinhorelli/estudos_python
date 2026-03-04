
def calcular_media(lista):
    quantidade = len(lista)
    soma = 0
    for c in lista:
        soma += c
    media = soma / quantidade
    return media
    
numeros = [6, 8, 7, 10, 19, 200]
media = calcular_media(numeros)
print(media)