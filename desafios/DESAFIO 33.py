print('========== DESAFIO #33 ==========')
n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))
n3 = float(input('Digite um terceiro número:'))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n2
if n1 > n2 and n1 > n3:
    maior = n1
if n3 > n1 and n3 > n2:
    maior = n3
print('O número {} é o maior número digitado'.format(maior))
print('O número {} é o menor número digitado'.format(menor))