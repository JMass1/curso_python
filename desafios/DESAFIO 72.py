#ESCREVENDO NUMEROS POR EXTENSO

num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

n = int(input('Digite um numero entre 0 - 20: '))
while n < 0 or n > 20:
    n = int(input('Numero incorreto, tente novamente. Digite um numero entre 0 - 20: '))
print(f'Voce digitou {num[n]}.')
