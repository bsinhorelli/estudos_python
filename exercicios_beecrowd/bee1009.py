vendendor = input('')
fixo = float(input(''))
total_vendas = float(input(''))

comissao = (15/100)* total_vendas
salario_total = comissao + fixo

print(f'TOTAL = R$ {salario_total:.2f}')

