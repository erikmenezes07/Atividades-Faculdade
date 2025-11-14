while True:
    try:

        nome = input("Digite seu nome: ")

        if nome.strip() == "":
            raise ValueError("O nome não pode ficar vazio.")

        if any(char.isdigit() for char in nome):
            raise ValueError("O nome não pode ter números.")

        idade_input = input("Digite sua idade: ")

        if any(char.isalpha() for char in idade_input):
            raise ValueError("A idade não pode ter letras.")

        idade = int(idade_input)

        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")

        print(f"\nNome: {nome}\nIdade: {idade} anos")
        break

    except ValueError as erro:
        print("Erro:", erro)
