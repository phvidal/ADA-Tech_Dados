"""
Considera a população da cidade X igual 75340 habitantes, sendo que esta cidade tem uma taxa de crescimento anual de 3.7%. 
A cidade Y tem uma população de 213480 habitantes com uma taxa de crescimento anual de 1.7%. 
Faça um código que informe em quantos anos a população da cidade X ultrapassará a cidade Y.

"""

x = 75340
tX = 0.037

y = 213480
tY = 0.017

cont = 0

while x < y:
  x += x * tX
  y += y * tY
  cont += 1

print(f"Em {cont} anos a Cidade X terá {x:.2f} habitantes, enquanto a Cidade Y terá {y:.2f} habitantes.")