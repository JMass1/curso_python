print('========== DESAFIO #49 ==========')
n1 = int (input('Digite um número inteiro'))
c = int()
print('A tabuada do número {} é:'.format(n1))
for c in range (1,11):
    print('{:<3} x   {:<2}  = {:>3}'.format(n1,c,n1*c))


#SOLUÇÃO COM USO DE LISTAS
n2 = int (input('Digite um número inteiro'))
c1 = int()
print('A tabuada do número {} é:'.format(n2))
tabuada = [c1*n2 for c1 in range (1,11)]
print(tabuada)
