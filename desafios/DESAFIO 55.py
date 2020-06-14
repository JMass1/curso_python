maior = float()
menor = float()
for i in range(1, 6):
    peso = float(input('Digite o {}º peso:'.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('De todos os pesos digitados, o maior foi: {} e o menor foi: {}'.format(maior, menor))
