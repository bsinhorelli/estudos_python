alunos = dict()

alunos['nome'] = input('Nome do aluno: ')
alunos['média'] = float(input('Média do aluno: '))

if alunos['média'] >= 7.0:
    alunos['situação'] = 'aprovado!'
else:
    alunos['situação'] = 'reprovado!'
    
for k, v in alunos.items():
    print(f'{k} é igual a {v}')