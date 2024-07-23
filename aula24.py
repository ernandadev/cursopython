# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 7 8
#  V a l e n t i n e
# -9-8-7-6-5-4-3-2-1

#nome = 'Valentine'
# print(nome[1])
# print(nome[-8])
#print('a' in nome) # True
#print('z' in nome) # False
#print('val' not in nome)


nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')