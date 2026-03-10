# listas
completa = []
pares = []
impares = []

# Estrutura para adicionar os números a lista completa
while True:
    num = int(input('Digite um número: '))
    completa.append(num)
    
    opcao = input('Quer continuar? [S/N] ')
    if opcao.lower() == 'n':
        print('Programa encerrando...')
        break

# dividindo os numeros da lista completa para a lista pares e impares
for numero in completa:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# resultado
print(f'A lista completa é: {completa}')
print(f'A lista pares é: {pares}')
print(f'A lista impares é: {impares}')
