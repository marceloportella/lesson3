# texto = "hoje e nossa terceira aula de bootcamp , do bootcamp python"

# palavras = texto.split()

# print(palavras)

# Desafio

nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is False:
    try:
        nome=input("Digite seu nome: ")
        #Verificar se o nome está vazio
        if len(nome.strip()) == 0:
            raise ValueError("O nome não pode estar vazio.")
        #Verificar se há numeros no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")

        else:
            print("Nome válido: ", nome)
            nome_valido = True
    except ValueError as e:
        print(e)
        #exit() -> inclua o exit caso queira abortar, ou seja vai sair do while

while salario_valido is False:
    try:
        salario = float(input("Digite seu salario: "))
        if salario < 0:
            print("Digite um valor positivo para o seu salario.")
        else:
            print(f"O seu salário é {salario}")
            salario_valido = True
    except ValueError:
        print("Entrada invalida para o salario, digite um numero")

while bonus_valido is False:
    try:
        bonus = float(input("Digite o bonus: "))
        if bonus < 0:
            print("Digite um valor positivo")
        else:
            bonus_valido = True
    except ValueError:
        print("Entrada invalida para bonus. Digite um numero. ")

kpi = ((bonus/100) * salario) + salario
print(f"O total é {kpi:.2f}")