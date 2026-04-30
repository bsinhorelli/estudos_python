voluntarios = []

while True:
    escolha = str(input('Digite o nome do voluntário (ou "sair" para encerrar): '))
    
    if escolha != 'sair':
        voluntarios.append(escolha)
        
    else:
        print('encerrando programa...')
        break
        
print(f'Voluntários Registrados: {voluntarios}')
