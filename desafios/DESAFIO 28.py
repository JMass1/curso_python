from random import randint
print('========== DESAFIO #28 ==========')
n1 = int(randint(0,5))
print(n1)
n2 = int(input('Tente adivinhar qual número escolhido pelo computador entre 0 e 5'))
if n1 == n2:
    print('Parabens! Você acertou o número.')
else:
    print('Que pena tente novamente!')