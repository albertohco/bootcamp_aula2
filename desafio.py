# Desafio - Refatorar o projeto da aula anterior evitando Bugs!
CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome

try:
    nome = input("Digite seu nome: ")
    if nome.isdigit():
        raise ValueError("Você digitou o nome errado")
    elif len(nome) == 0:
        raise ValueError("Você não digitou nada")
    elif nome.isspace():
        raise ValueError("Você digitou só espaço")
    else:
        print(f"Nome válido, {nome} ")
except ValueError as e:
    print(e)
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario = float(input("Digite seu salario: "))
    if salario < 0:
        raise ValueError(
            "você digitou um sálario menor que zero, digie um valor positivo")
    elif salario == 0:
        raise ValueError(
            "você digitou um sálario igual a zero, digie um valor positivo")
except ValueError as e:
    print(e)
    exit()

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus = float(input("Digite seu bonus: "))
    if bonus < 0:
        raise ValueError(
            "você digitou um bonus menor que zero, digie um valor positivo")
    elif bonus == 0:
        raise ValueError(
            "você digitou um bonus igual a zero, digie um valor positivo")
except ValueError as e:
    print(e)
    exit()

# 4) Calcule o valor do bônus final
kpi = CONSTANTE_BONUS + salario * bonus

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá {nome}, o seu bônus foi de {kpi}")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
