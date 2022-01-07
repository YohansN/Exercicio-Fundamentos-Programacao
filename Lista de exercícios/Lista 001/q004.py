'''Q004: Construa um algoritmo para calcular as raízes de uma equação do 2o. Grau (ax2 + bx + c), sendo que A, B, e C
são valores fornecidos pelo usuário.'''

a = int(input("a:"))  
b = int(input("b:"))
c = int(input("c:"))
Delta = (b)**2 -4*a*c
raiz_delta = (Delta)**(1/2)
X1 = (-b + raiz_delta) / (2*a)
X2 = (-b - raiz_delta) / (2*a)
print(f"Raizes: x1:{X1} | x2:{X2}")
