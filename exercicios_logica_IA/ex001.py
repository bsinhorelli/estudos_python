# Entrada do Usuário
num = int(input('Digite um número inteiro: '))

# Laço para percorrer numéros pares de 0 até a entrada do usuário
for c in range(0, num+1):
    if c % 2 == 0:
        print(c)