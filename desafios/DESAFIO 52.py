n = int(input('Digite um número:'))
count = int()
for i in range(2, n):
    if n%i == 0:
        count += 1
if count > 0:
    print('O número digitado não é primo')
else:
    print('O número digitado é primo')

#SOLUÇÃO ALTERNATIVA
i = 0
n1 = int(input('Digite um número:'))
count = 0
for i in range(1, n1+1):
    if n1%i == 0:
        print('\033[33m {} '.format(i), end='')
        count += 1
    else:
        print('\033[31m {} '.format(i), end='')
if count > 2:
    print('\nO número digitado não é primo')
else:
    print('\nO número digitado é primo')