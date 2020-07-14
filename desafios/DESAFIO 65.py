#PROGRAMA PARA LER N ENTRADAS E EXIBIR A CONTAGEM DE ENTRADAS, A MEDIA ENTRE AS ENTRADAS, MAIOR E MENOR NUMERO DIGITADO

i = tot = num = maior = menor = 0
a = ''
while a != 'n':
    num = int(input('Digite um numero: '))
    a = str(input('Quer continuar [s/n]?')).lower().strip()
    tot += num
    i += 1
    if i == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('Voce digitou {} numeros, a media foi de {}.'.format(i, tot/i))
print('O maior numero digitado foi {} e o menor {}.'.format(maior, menor))
