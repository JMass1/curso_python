a1 = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
n = int(input('Digite o número de termos desejado:'))
lista = []
pa = int(a1)
i = int(1)
while n >= i:
    lista.append(pa)
    pa += r
    i += 1
print('Os {} primeiros termos da PA são:'.format(n))
print(lista)