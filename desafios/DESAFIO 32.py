print('========== DESAFIO #32 ==========')
iano = int(input('Digite um ano:'))
if iano%400==0:
    print('O ano de {} é bisexto.'.format(iano))
elif iano%100==0:
    print('O ano de {} não é bisexto'.format(iano))
elif iano%4==0:
    print('O ano de {} é bisexto.'.format(iano))
else:
    print('O ano de {} não é bisexto'.format(iano))