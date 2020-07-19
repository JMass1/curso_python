#APRENDENDO SOBRE TUPLAS:

cb20 = ('palmeiras', 'sao paulo', 'santos', 'corinthians', 'fluminense', 'flamengo', 'cruzeiro', 'atletico mineiro', 'vasco', 'ponte', 'chapecoense', 'gremio', 'inter', 'vitoria', 'atletico paranaense', 'coritiba', 'bota fogo', 'goias', 'bahia', 'ceara')
print('A) Primeiros 5 colocados:')
print(cb20[0:5])

#Segunda opcao
'''for i in range(0, 5, 1):
    print(f'{cb20[i]}')'''

print('\nB) Ultimos 4 colocados:')
print(cb20[-4:])

#Segunda opcao
'''for i in range(-4, -0, 1):
    print(f'{cb20[i]}')'''

print('\nC) Lista dos Times em ordem alfaberica:')
print(sorted(cb20))
print('\nD) Colocacao da Chapecoense na tabela:')
print(f'{cb20.index("chapecoense")+1} posicao')
