' DESAFIO 63 - ESCREVENDO A SEQUENCIA DE FIBONACCI'
i = int(0)
num = int(0)
num1 = int(1)
num2 = int(0)
n = int(input('Digite o numero de termos que quer mostrar: '))
print('{} '.format(num))
while i < n-1:
    num = num1 + num2
    num1 = num2
    num2 = num
    print('{} '.format(num))
    i += 1
