#LISTA DE PRODUTOS SUPERMERCADO

lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Sabão em pó', 22.00)

print('-'*45)
print(f'{"LISTA DE PREÇOS":^45}')
print('-'*45)
for i in range(0, len(lista), 2):
    print(f'{lista[i]:.<30}',end='')
    print(f'R${lista[i+1]:>8.2f}')
