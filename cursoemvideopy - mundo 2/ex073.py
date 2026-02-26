tabela_brasileirao_2023 = (
    "Palmeiras", "Grêmio", "Atlético Mineiro", "Flamengo", "Botafogo",
    "Red Bull Bragantino", "Fluminense", "Athletico Paranaense", "Internacional", "Fortaleza",
    "São Paulo", "Cuiabá", "Corinthians", "Cruzeiro", "Vasco da Gama",
    "Bahia", "Santos", "Goiás", "Coritiba", "América Mineiro"
)

print('\na) Os 5 Primeiros são:')
for c in tabela_brasileirao_2023[0:5]:
    print(c, end=(' | '))

print('\n\nb) Os últimos 4 colocados:')
for u in tabela_brasileirao_2023[-4:]:
    print(u, end=(' | '))

print('\n\nc) Times em ordem alfabética:')
print(sorted(tabela_brasileirao_2023))

print('\nd) Em que posição está o corinthians:')
print(tabela_brasileirao_2023.index('Corinthians'))






