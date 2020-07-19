#TRABALHANDO COM LISTAS
lista = []
for i in range(0,5):
    lista.append(int(input(f'Digite um numero para a posicao {i+1}: ')))
    if i == 0:
        maior = lista[i]
        menor = lista[i]
    elif lista[i] > maior:
        maior = lista[i]
    elif lista[i] < menor:
        menor = lista[i]
print(f'Dentro dos numeros digitados {lista}: ')
print(f'O menor numero digitado foi: {menor} e ele aparece nas posicoes: ',end='')
i = c = 0
for c, i in enumerate(lista):
    if i == menor:
        print(f'{c+1}...',end='')
print(f'\nO maior numero digitado foi: {maior} e ele esta nas posicoes: ', end='')
i = c = 0
for c, i in enumerate(lista):
    if i == maior:
        print(f'{c+1}...',end='')
