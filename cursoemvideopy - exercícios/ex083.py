expr = input('Digite uma expressão: ')
pilha = []
for simb in pilha:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
    else:
        pilha.append(')')
        break

if len(pilha) == 0:
    print('A expressão é valida!')
else:
    print('Expressão Inválida!')