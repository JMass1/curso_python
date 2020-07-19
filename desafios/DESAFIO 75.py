#IMPUTANDO VALORES EM TUPLAS

num = (int(input('Digite um valor:')), int(input('Digite outro valor:')), int(input('Digite mais um valor:')), int(input('Digite um quarto valor:')))
print(f'Os numeros digitados foram {num}.')
print(f'O numero 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O numero 3 apareceu na {num.index(3)+1} posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posilção.')
print(f'Os valores pares digitados foram:', end='')
for i in num:
    if i%2 == 0:
        print(f'{i} ', end='')
