

def contar_vogais(texto):
    vogais = 'aeiou'
    soma = 0
    for c in texto.lower():
        if c in vogais:
            soma += 1
    return soma

texto = input('Digite alguma coisa: ')
soma = contar_vogais(texto)
print(soma)


    