# EXERCICIO
# peça ao usuário para digitar seu nome
# peça ao usuário para digitar sua idade
# se o nome e idade forem digitados:
# exiba:
# seu nome é {nome}
# seu nome invertido é {nome invertido}
# seu nome contém (ou não) espaços
# seu nome tem {n} letras
# a primeira letra do seu nome é {letra}
# a última letra do seu nome é {letra}
# se nada for digitado em nome ou idade:
# exiba 'Desculpe, você deixou campos vazios.'


# COMO EU FIZ A ATIVIDADE:

nome = input('Digite seu nome: ')
idade = input('Digite Sua idade: ')
print(f'Seu nome é {nome}')
print(f'Sua idade é {idade}')
print(f'Seu nome invertido é', (nome [-1::-1]))
numero_de_caracteres = len(nome)
print(f"O seu nome '{nome}' tem {numero_de_caracteres} letras.")
if " " in nome:
    print(f"O nome '{nome}' contém espaços.")
else:
    print(f"O nome '{nome}' não contém espaços.")
primeira_letra = nome[0]
print(f"A primeira letra do nome '{nome}' é '{primeira_letra}'.")
ultima_letra = nome[-1]
print(f"A última letra do nome '{nome}' é '{ultima_letra}'.")


#COMO O PROFESSOR CORRIGIU:
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios")
