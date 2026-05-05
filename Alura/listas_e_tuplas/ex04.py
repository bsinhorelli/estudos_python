estoque1 = tuple(input('Produtos do estoque 1 (separados por vírgula): ').split())
estoque2 = tuple(input('Produtos do estoque 2 (separados por vírgula): ').split())

estoque_combinado = estoque1 + estoque2

print(f'Estoque 1: {estoque1}')
print(f'Estoque 2: {estoque2}')
print(f'\nEstoque Combinado: {estoque_combinado}')
