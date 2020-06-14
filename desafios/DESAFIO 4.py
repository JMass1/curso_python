print('========== DESAFIO #4 ==========')
var: str = input('Digite algo')
print('Você digitou: {}'.format(var))
print('O tipo primitivo do que você digitou é {}'.format(type(var)))
if var.isnumeric():
    print('O que você digitou é numérico')
if var.isalpha():
        print('O que você digitou é alfabético')
