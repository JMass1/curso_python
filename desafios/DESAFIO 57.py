sexo = str(input('Digite seu sexo(F ou M):')).strip().upper()
i = int(1)
while i!=0:
    if sexo in 'M':
        i = 0
        print('O sexo digitado foi masculino')
    if sexo in 'F':
        i = 0
        print('O sexo digitado foi feminino')
    else:
        sexo = str(input('Dado invalido, informe novamente seu sexo(F ou M):')).strip().upper()


#SEGUNDA OPCAO
sexo1 = str(input('Digite seu sexo(F ou M):')).strip().upper()[0]
while sexo1 not in 'FM':
    sexo1 = str(input('Dado invalido, informe novamente seu sexo(F ou M):')).strip().upper()[0]
print('O sexo {} registrado com sucesso'.format(sexo1))
