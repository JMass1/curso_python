print('========== DESAFIO #50 ==========')
cont = int()
soma = int()
for c in range(1, 7):
    n1 = int(input('Digite seu {}º número'.format(c)))
    if n1%2 == 0:
        cont += 1
        soma += n1
print('Você digitou {} número pares, a soma deles é de {}'.format(cont, soma))
