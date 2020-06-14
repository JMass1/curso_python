print('========== DESAFIO #51 ==========')

a1 = int(input('Digite o primeiro termo da PA:'))
r = int(input('Digite a razão da PA:'))
n = int(input('Digite o número de termos desejado:'))
pa = [a1+i*r for i in range(0, n)]
print('Os {} primeiros termos da PA são:'.format(n))
print(pa)

#SEGUNDA POSSIBILIDADE
i = 0
prim = int(input('Digite o primeiro termo da PA:'))
raz = int(input('Digite a razão da PA:'))
nterm = int(input('Digite o número de termos desejado:'))
termn = prim+(nterm-1)*raz
pa1 = [i for i in range(prim, termn+raz, raz)]
print('Os {} primeiros termos da PA são:'.format(nterm))
print(pa1)