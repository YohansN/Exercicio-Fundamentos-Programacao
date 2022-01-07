'''Q002: Faça um algoritmo que receba o raio R de uma esfera e calcule o seu volume: V = (4 * Pi * R3)/3.'''

pi = 3.14 #pi aproximado
Raio = float(input("Raio: "))
V = (4 * pi * Raio**3)/3
print(f"O valor da esfera é: {V:.2f}")
