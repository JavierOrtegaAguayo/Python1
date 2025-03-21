"""
En este codigo vamos a ver la sintaxis basica de python
21-03-25
"""

#! Sintaxis de python

#? Identacion

# a = 10
# b = 5

# if b > a:
#     print("b es mayor que a") 
    
#? Variables

# Para funciones iniciamos con mayusc

# precio_cu = 4.5
# p_cu = 4.5

# x = 10 #Interger ---> numero entero
# y = 10.0 #Float
# print(type(x))
# print(type(y))

# nombre = "Juan"
# print(type(nombre))

# x = 10
# x = float(x)
# x = 10.5
# x = int(x)
# print(x)

# x, y, z = 15, 20.3, "Juan"
# print(x, y, z)

#? Estructuras de control

#x, y, z = 10, 20, 30

# if x > y:
#     print("x es mayor que y")
# elif y > x:
#     print("y es mayor que x")
# elif z > x:
#     print("z es mayor que x")
# else:
#     print("no se cumple nada")    

# Ciclos
# for x in range(5, 20 + 1, 5):
#     print(x)
#     if x < 15:
#         print("x es menor a 15")
        

# while x > 10:
#     print("x es mayor a 10")

#? Funciones

# def Suma(a, b):
#     resultado = a + b
#     return resultado

# sumando = Suma(5, 10)
# print(sumando)
# print(3)

#? Excepciones
# try, except, finally

# try:
#     resultado = 10/0
# except ZeroDivisionError:
#     print("Imposible dividir por cero")
# finally:
#     print("Fin del bloque try")

#? Librerias

# import math
# a = math.sqrt(16)
# print(a)

# from math import sqrt
# a = sqrt(16)
# print(a)

#? Operadores comunes
# aritmeticos
# +; -; *; /; // (division entera): % (modulo); ** (potencia)

# comparacion
# >; <; ==; >=; <=; !=

if 4 != 5:
    print("4 es diferente a 5")

# logicos
# and; or; not

# operadores booleanos

#? Listas y diccionarios

