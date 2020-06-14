from math import hypot
print('========== DESAFIO #17 ==========')
catad = float(input('Informe cateto adjacente:'))
catop = float(input('Informe cateto oposto:'))
hipot = hypot(catad,catop)
hipot2 = (catad**2+catop**2)**(1/2)
print('O valor da hipotenusa é de: {}, que é igual contraprova: {}'.format(hipot, hipot2))