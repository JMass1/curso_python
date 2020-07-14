# PROGRAMA PARA IMPRIMIR A TABUADA DE UM DADO NUMERO

n = 1
num = 0
while True:
    print('-'*30)
    num = int(input('Quer saber a tabuada de qual valor? '))
    print('-'*30)
    while n <= 10:
        print(f'{num}  *  {n:<2}   =   {num*n}')
        n += 1
    if num < 0:
        break
