from random import randint
n1 = int(randint(0,10))
n2 = int(11)
count = int()
while n2 != n1:
    n2 = int(input('Tente adivinhar qual número escolhido pelo computador entre 0 e 10.\n'))
    count += 1
    if n2 > n1:
        print('Um pouco menos')
    else:
        print('Fala um pouco mais...')
print('Parabens! Você acertou o número apos {} tentativas.'.format(count))