# Interpolação básica de strings
# s - string
# d e i - int
# f - foat
# .<número de dígitos>f
# x e X - Hexadecimal (ABCDEF0123456789)
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# = - força o número a aparecer antes dos zeros
# Sinal - + ou -
# Ex.: 0>-100,. 1f
# Conversion flags - !r !s !a 
# """
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.270502}')
print(f'{1000.270502:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08x}')