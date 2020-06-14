print('========== DESAFIO #36 ==========')
print('Programa de Emprestimos Banco Capiroto!!!\n   ')

fvalorcasa = float(input('Qual o valor total da casa que deseja financiar?'))
fvalorsal = float(input('Qual o valor de seu salário mensal?'))
inumprest = int(input('Em quantos anos deseja parcelar a casa?'))

fvalorprest = fvalorcasa/inumprest/12
if fvalorsal*0.3>fvalorprest:
    print('\033[1;32m O emprestimo foi aprovado, sua parcela será de R${}'.format(fvalorprest))
else:
    print('\033[1;31m Infelizmente o empréstimo foi negado, devido as parcelas serem maiores que 30% de seu salário')