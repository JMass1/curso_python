print('========== DESAFIO #48 ==========')
soma = int(0)
cont = int (0)
for c in range(3,496,3):
    if c%2 != 0:
        cont += 1
        soma += c
print('A soma dos {} valores solicitados é {}'.format(cont,soma))

## Solução com uso de LISTA:

i = int()

nums = [i for i in range(3, 496,3) if i % 2 !=0] ## (CRIA LISTA COM AS CONDIÇÕES DO ENUNCIADO)

print('\n A soma dos {} ímpares múltiplos de 3 entre 1 e 500 é igual a {}.'.format(len(nums), sum(nums)))