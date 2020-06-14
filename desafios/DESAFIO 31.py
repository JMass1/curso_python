print('========== DESAFIO #31 ==========')
fdist = float(input('Qual a distância em km de sua viagem?'))
if fdist>200:
    print('O valor de uma passagem para uma viagem de {}km é de R${:.2f}'.format(fdist,fdist*0.45))
else:
    print('O valor de uma passagem para uma viagem de {}km é de R${:.2f}'.format(fdist, fdist * 0.50))
