print('========== DESAFIO #25 ==========')
sn = str(input('Qual seu nome completo?')).strip()
print('Seu nome tem Silva?',end='')
print(sn.lower().find('silva')>-1)
# SEGUNDA OPÇÃO
print('silva' in sn.lower())