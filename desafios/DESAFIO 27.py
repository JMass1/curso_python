print('========== DESAFIO #27 ==========')
snome = str(input('Digite seu nome completo')).strip()
asnome = snome.split()
iqtde = int(len(asnome)-1)
print('primeiro: {}'.format(asnome[0]))
print('ultimo: {}'.format(asnome[iqtde]))

#SEGUNDA OPÇÃO
print('ultimo: {}'.format(asnome[len(asnome)-1]))
