"""

Receba do usuário um número inteiro positivo e o retorne invertido.
Exemplo: Valor recebido 12345, resultado 54321

"""

# num_usr = input('Digite um número: ')

# print(int(num_usr[::-1]))

numero = int(input("Informe uma sequencia de numeros: ")) # 12345

numero_invertido = 0
numero_original = numero

while numero > 0:
  digito = numero % 10 # 12345 % 10 = 3 --->> 12345 % 10 = 12,3
  numero_invertido = numero_invertido * 10 + digito #numero_invertido = 543
  numero = numero // 10 # 1234 // 10 = 123

print(f"o número {numero_original} invertido é: {numero_invertido}")

