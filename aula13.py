nome = "Valentine Pelissari"
altura = 1.56
peso = 62
imc = peso / (altura ** 2)

#f-strings = formatação de strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc}'
print(linha_1)
print(linha_2)
print(linha_3)