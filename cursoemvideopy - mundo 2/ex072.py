numeros = (
    "zero", "um", "dois", "três", "quatro",
    "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze",
    "quinze", "dezesseis", "dezessete", "dezoito",
    "dezenove", "vinte"
)

while True:
    escolha = int(input('Digite um número de 0 a 20: '))
    if escolha > 0 and escolha < 20:
        break
    print('Tente novamente com um valor válido!')

print(f'O numero escolhido por extenso é {numeros[escolha]}')
