"""
Faça um programa que recebe as coordenadas e encontra a distância entre dois pontos em um plano cartesiano (x e y)

Dica: O Teorema de pitágoras pode te ajudar

"""

# hipotenusa = raiz_quadrada(cateto_a**2 + cateto_b**2)

# ponto_x = float(input('Passe sua localidade: '))
# ponto_y = float(input('Passe sua localidade: '))

x1 = float(input('Digite a coordenada x1 do primeiro ponto: '))
x2 = float(input('Digite a coordenada x2 do primeiro ponto: '))
y1 = float(input('Digite a coordenada y1 do primeiro ponto: '))
y2 = float(input('Digite a coordenada x1 do primeiro ponto: '))

distancia_x = x2-x1 #isso representa o primeiro cateto
distancia_y = y2-y1 #isso representa o segundo cateto

soma_quadrado_catetos = (distancia_x ** 2) + (distancia_y ** 2)
distancia = soma_quadrado_catetos**(1/2)

print(f'A distância entre os pontos é: {distancia:.2f}')