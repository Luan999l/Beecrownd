# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B. 


a,b,c = list(map(float,input().split()))
triangle=0.5*a*c
circle=3.14159*c*c
trapezium=(a+b)/2.0*c
square=b*b
rectangle=a*b
print("TRIANGULO: %.3lf"%triangle)
print("CIRCULO: %.3f"%circle)
print("TRAPEZIO: %.3f"%trapezium)
print("QUADRADO: %.3f"%square)
print("RETANGULO: %.3f"%rectangle)