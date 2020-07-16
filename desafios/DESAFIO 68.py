#PROGRAMA QUE EMULA O JOGO DE PAR OU IMPAR
from random import randint
nump = numc = tot = 0
pn = ''
countv = 0
print('=-'*20)
print('Vamos jogar par ou impar?')
print('=-'*20)
while True:
    nump = int(input('Digite um número: '))
    pn = str(input('Par ou Impar [P/I]? ')).strip().upper()
    print('-'*40)
    numc = 2#randint(0,10)
    tot = nump + numc
    if tot%2 == 0:
        print(f'Você jogou {nump} e o computador {numc}. Total de {tot} deu par!')
        print('-'*40)
        if pn == 'P':
            countv += 1
            print(f'Você venceu, vamos jogar novamente...')
            print('-'*40)
        else:
            print('Se fodeo!!!')
            print('-'*40)
            break
    else:
        print(f'Você jogou {nump} e o computador {numc}. Total de {tot} deu impar!')
        if pn == 'I':
            countv += 1
            print(f'Você venceu, vamos jogar novamente...')
            print('-'*40)
        else:
            print('Se fodeo!!!')
            print('-'*40)
            break
print(f'GAME OVER! Você ganhou {countv} jogos!')
