from math import fabs
print('========== DESAFIO #35 ==========')
l1 = int(input('Digite o primeiro lado do triangulo:'))
l2 = int(input('Digite o segundo lado do triangulo:'))
l3 = int(input('Digite o terceiro lado do triangulo:'))

if fabs(l2-l3)<l1 and l1<l2+l3:
    if fabs(l1-l3)<l2 and l2<l1+l3:
        if fabs(l1 - l2) < l3 and l3 < l1 + l2:
            print('É possível montar um triangulo com os valores digitados')
else:
    print('Não é possível montar um triangulo com os valores digitados')