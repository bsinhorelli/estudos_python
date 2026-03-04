numeros = []
rodando_programa = True

while rodando_programa:
    print('1 - Listar número')
    print('2 - Exibir Lista')
    print('3 - Sair')
    
    opcao = int(input('Escolha uma opção: '))
    
    # usuário escolhe um número e adiciona ele a lista
    if opcao == 1:
        rodando_listar = True
        while rodando_listar:
            print('1 - Adicionar número inteiro\n2 - Voltar ao menu')
            opcao_listar = int(input('Escolha uma opção: '))
            if opcao_listar == 1:
                num = int(input('\nAdicionar número inteiro a lista: '))
                numeros.append(num)
                print(f'{num} adicionado com sucesso!\n')
            elif opcao_listar == 2:
                print('Voltando ao menu...')
                rodando_listar = False
                
    
    # usuário exibe a lista
    elif opcao == 2:
        print(f'\nNúmeros inteiros: {numeros}')
    
    #usuário encerra o programa
    elif opcao == 3:
        print('Programa encerrado!')
        rodando_programa = False
        
    
        
