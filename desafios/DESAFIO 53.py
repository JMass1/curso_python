frase = str(input('Digite uma frase')).strip().upper().replace(' ', '')
fim = len(frase)
count = int()
for i in range(0, (fim//2)+1):
    if frase[i] == frase[(fim-1)-i]:
        count += 1
if count-1 == i:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')

#SEGUNDA POSSIBILIDADE
i = 0
frase1 = str(input('Digite uma frase')).strip().upper().replace(' ', '')
inverso = ''
for i in range(len(frase1)-1, -1, -1):
    inverso += frase1[i]
if frase1 == inverso:
    print('A frase digitada é um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')