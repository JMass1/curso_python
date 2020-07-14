# PROGRAMA PARA CONTAR NUMERO DE ENTRADAS E EXIBIR NUMERO DE ENTRADAS E SOMA DAS ENTRADAS
i = 0
IN = 0
tot = 0
while IN != 999:
    IN=int(input('Digite um numero ou "999" para parar: '))
    if IN != 999:
        tot += IN
        i += 1
print('Foram digitados {} numeros, somando os valores digitados temos {}.'.format(i, tot))
