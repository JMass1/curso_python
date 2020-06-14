from random import randrange
print('========== DESAFIO #29 ==========')
v = float(randrange(0,300))
if v>80:
    print('Você passou a {}km/h em um radar do qual o limite de velocidade é de 80km/h, sua multa será de R${}'.format(v,(v-80.0)*7.0))
