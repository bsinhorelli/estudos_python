from datetime import datetime

pessoa = dict()

pessoa['nome'] = input('Nome: ')
ano_nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - ano_nascimento
pessoa['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - datetime.now().year)
else:
    print('Não Possui CTPS!')
print('-='*30) 
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')
