count = int()
for i in range(1, 8):
    idade = int(input('Digite a idade da {}ª pessoa'.format(i)))
    if idade >= 18:
        count += 1
print('{} pessoas ainda não atingiram a maioridade e {} já.'.format(7-count, count))