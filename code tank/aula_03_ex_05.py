"""
5) Faça um script que peça para o usuário digitar a idade, o salário e o sexo de uma pessoa até que as entradas digitadas sejam válidas.

a. Idade: entre 0 e 150
b. Salário: maior que 0
c. Gênero: M, F ou Outro

Por último imprima os dados recebidos do usuário.

"""

idade = int(input("Digite a idade: "))
while idade < 0 or idade > 150:
    print("Idade fora do intervalo válido (0 a 150). Tente novamente.")
    idade = int(input("Digite a idade: "))

salario = float(input("Digite o salário: "))
while salario <= 0:
    print("Salário deve ser maior que 0. Tente novamente.")
    salario = float(input("Digite o salário: "))

genero = input("Digite o gênero (M, F ou Outro): ").strip().upper()
while genero not in ('M', 'F', 'OUTRO'):
    print("Gênero inválido. Tente novamente.")
    genero = input("Digite o gênero (M, F ou Outro): ").strip().upper()

print("\nDados recebidos:")
print(f"Idade: {idade} anos")
print(f"Salário: R$ {salario:.2f}")
print(f"Gênero: {genero}")

    