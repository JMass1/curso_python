import random
print('========== DESAFIO #19 e 20 ==========')
nome1 = input('Digite primeiro nome:')
nome2 = input('Digite segundo nome:')
nome3 = input('Digite terceiro nome')
nome4 = input('Digite quarto nome')
lista = [nome1,nome2,nome3,nome4]
random.shuffle(lista)
print('O aluno sorteado para apagar o quadro foi: {}'.format(random.choice(lista)))
print('A ordem de apresentação será: {}'.format(lista))
