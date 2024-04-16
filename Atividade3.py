# Maioridade para dirigir
maioridade_cnh_eua = 16
maioridade_cnh_brasil = 18

ano_nascimento = int(input("Qual seu ano de nascimento? Ex.: 1952 "))
cnh = input("Você possui CNH?\nResponda S para 'SIM' ou N para 'Não': ")

idade = 2024 - ano_nascimento

if cnh == 'S':
    if idade >= maioridade_cnh_brasil:
        print(f"Você tem {idade} anos, possui carteira e está apto a dirigir no Brasil e nos Estados Unidos!")
    elif idade >= maioridade_cnh_eua:
        print(f"Você tem {idade} anos, possui carteira e está apto a dirigir nos Estados Unidos!")
else:
    if idade >= maioridade_cnh_brasil:
        print(f"Você tem {idade} anos, estaria apto a dirigir no Brasil e nos Estados Unidos, mas não possui carteira!")
    elif idade >= maioridade_cnh_eua:
        print(f"Você tem {idade} anos, estaria apto a dirigir nos Estados Unidos, mas não possui carteira!")
    else:
        print(f"Você não está apto a dirigir!")
    




