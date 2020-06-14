n = int(input('Digite um numero para saber seu fatorial:'))
print('O fatorial de {} e:'.format(n))
fat = n
print('{}! = {}'.format(n, n), end='')
n -= 1
while n != 0:
    print(' x {}'.format(n), end='')
    fat *= n
    n -= 1
print(' = {}.'.format(fat))