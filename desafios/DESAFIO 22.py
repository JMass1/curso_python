print('========== DESAFIO #22 ==========')
n = str(input('Digite seu nome completo')).strip()
nl = n.split()
print('Nome maiusculo: {}'.format(n.upper()))
print('Nome minusculo: {}'.format(n.lower()))
print('Quantidade de letras sem considerar o espaço: {}'.format(len(n.replace(' ',''))))

#MANEIRA OPCIONAL
print('Quantidade de letras sem considerar o espaço: {}'.format(len(n)-n.count(' ')))

print('Quantidade de letras do primeiro nome: {}'.format(len(nl[0])))

#MANEIRA OPCIONAL
print('Quantidade de letras do primeiro nome: {}'.format(n.find(' ')))