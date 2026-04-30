while True:
    try:
        num = int(input('Digite um número: '))
        dobro = num *2
        print(dobro)
        break
    except:
        print('Entrada inválida, digite um número inteiro!')
    finally:
        print('Obrigado, Volte Sempre!')