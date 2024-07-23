"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


numero = input("Digite um número inteiro: ")
try:
  numero = int(numero)
  if numero % 2 == 0:
      print(f"O número {numero} é par")
  else:
      print(f'O número {numero} é ímpar')
except:
  print('Você não digitou um número inteiro.')

  
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


hora = input('Que horas são? ')
try:
    if 00 <= int(hora) <= 11:
        print('Bom dia!')
    elif 12 <= int(hora) <= 17:
        print('Boa tarde!')
    elif 18 <= int(hora) <= 24:
        print('Boa noite!')
except:
    print('Nenhum número inteiro foi digitado.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual seu primeiro nome? ')
tamanho_nome = len(nome)

if tamanho_nome > 0:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    elif tamanho_nome > 4 and tamanho_nome <= 7:
        print('Seu nome é médio.')
    else:
        print('Seu nome é grande.')
else:
    print('Você não digitou um nome.')