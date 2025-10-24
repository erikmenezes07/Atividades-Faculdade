
nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("O nome deve ter mais que 3 caracteres.")
    nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Idade inválida! Digite entre 0 e 150.")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: "))
while salario <= 0:
    print("O salário deve ser maior que zero.")
    salario = float(input("Digite seu salário: "))

genero = input("Digite seu gênero (f/m): ").lower()
while genero not in ['f', 'm']:
    print("Gênero inválido! Use 'f' para feminino ou 'm' para masculino.")
    genero = input("Digite seu gênero (f/m): ").lower()

estado_civil = input("Digite seu estado civil (s, c, v, d): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']:
    print("Estado civil inválido! Use: s, c, v ou d.")
    estado_civil = input("Digite seu estado civil (s, c, v, d): ").lower()

print("\n Dados validados com sucesso!")
print(f"Nome: {nome}\nIdade: {idade}\nSalário: {salario}\nGênero: {genero}\nEstado Civil: {estado_civil}")
