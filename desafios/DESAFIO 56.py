soma = int()
idade1 = int()
nome1 = ''
count = int()
for i in range(1, 5):
    nome = str(input('Digite o {}º nome:'.format(i))).strip()
    idade = int(input('Digite a {}ª idade:'.format(i)))
    sexo = str(input('Digite o {}º sexo (m para masculino e f para feminino):'.format(i))).strip()
    soma += idade

    if sexo in 'mM':
        if i == 1:
            idade1 = idade
            nome1 = nome
        elif idade > idade1:
            idade1 = idade
            nome1 = nome
    if sexo in 'Ff':
        if idade < 20:
            count += 1
print('A média de idade do grupo é de {}'.format(soma/4))
print('O homem mais velho se chama {}'.format(nome1))
print('Desse grupo {} mulheres tem menos que 20 anos.'.format(count))