#PROGRAMA PARA SIMULAR UM CAIXA ELETRONICO

print('========= BANCO GAMBI =========')
saque = int(input('Qual valor deseja sacar? '))
while True:
    if saque > 49:
        print(f'Total de notas de R$50: {saque//50}')
        saque = saque%50
        if saque == 0:
            break
    if saque > 19:    
        print(f'Total de notas de R$20: {saque//20}')
        saque = saque%20
        if saque == 0:
            break
    if saque > 9:    
        print(f'Total de notas de R$10: {saque//10}')
        saque = saque%10
        if saque == 0:
            break
    print(f'Total de notas de R$1: {saque//1}')     
    break
print('-'*30)
print('Volte Sempre ao Banco Gambi!!!')
