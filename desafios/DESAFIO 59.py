from time import sleep
valor1 = float(input('Digite o primeiro numero:'))
valor2 = float(input('Digite o segundo numero:'))
valor3 = float()
operacao = int()
while operacao != 5:
    print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
    operacao = int(input('''Digite a operacao desejada:\n[1] Soma\n[2] Multiplicacao\n[3] Maior\n[4] Digitar novos numeros\n[5] Finalizar programa\n'''))
    if operacao == 1:
        valor3 = valor1 + valor2
        print('A soma entre {} e {} e igual a {}.\n'.format(valor1,valor2,valor3))
        sleep(2)
    if operacao == 2:
        valor3 = valor1 * valor2
        print('A multiplicacao entre {} e {} e igual a {}.\n'.format(valor1, valor2, valor3))
        sleep(2)
    if operacao == 3:
        if valor1 > valor2:
            print('O valor {} e maior que o valor {}.\n'.format(valor1, valor2))
            sleep(2)
        elif valor2 > valor1:
            print('O valor {} e maior que o valor {}.\n'.format(valor2, valor1))
            sleep(2)
        else:
            print('Os valores digitados sao iguais.\n')
            sleep(2)
    if operacao == 4:
        valor1 = float(input('Digite novamente o primeiro numero:'))
        valor2 = float(input('Digite novamente o segundo numero:'))
    if operacao > 5:
        print('Operacao invalida, tente novamente!.\n')
        sleep(2)