#PROGRAMA PARA CADASTRAR PRODUTOS E PREÇOS

preco = soma = count = mpreco = 0
nome = saida = nbarato = ''
while True:
    print('-'*20)
    print('CADASTRE UM PRODUTO')
    print('-'*20)
    nome = str(input('Nome do Produto: ')).strip()
    preco = int(input('Preço do Produto: '))
    print('-'*20)
    soma += preco
    if preco > 1000:
        count += 1
    if mpreco == 0:
        nbarato = nome
        mpreco = preco
    if mpreco > preco:
        nbarato = nome
        mpreco = preco
    saida = str(input('Quer Continuar [S/N]?')).strip().upper()
    while saida != 'S' and saida != 'N':
        saida = str(input('Quer Continuar [S/N]?')).strip().upper()
    if saida == 'N':
        break
print('-------FIM DO POGRAMA-------')
print(f'Total gasto em compras: {soma}.')
print(f'Ao todo temos {count} produtos com valor maior que R$1000.')
print(f'O produto de menor preço é: {nbarato}.')
