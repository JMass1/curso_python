#PROGRAMA PARA CADASTRAR DIVERSAS PESSOAS

idade = counta = countb = countc = 0
sexo = saida = ''
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
    print('-'*20)
    if idade > 18:
        counta += 1
    if sexo == 'M':
        countb += 1
    if sexo == 'F' and idade < 20:
        countc += 1
    saida = str(input('Quer Continuar [S/N]?')).strip().upper()
    while saida != 'S' and saida != 'N':
        saida = str(input('Quer Continuar [S/N]?')).strip().upper()
    if saida == 'N':
        break
print('-------FIM DO POGRAMA-------')
print(f'Total de pessoas maiores de 18 anos: {counta}.')
print(f'Ao todo temos {countb} homens cadastrados.')
print(f'E temos {countc} mulher(es) com menos de 20 anos.')
