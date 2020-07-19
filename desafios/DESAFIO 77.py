#TRABALHANDO COM TUPLAS

palavras = ('aprender', 'tomar', 'curso', 'gratis', 'python', 'estudar', 'praticar', 'mercado')
for i in palavras:
    print(f'\nNa palavra {i} temos as vogais: ', end='')
    for l in i:
        if l.lower() in 'aeiou':
            print(f'{l} ', end='')
print('')
