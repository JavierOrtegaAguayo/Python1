#EJERCICIO
#Aplanar una lista

#lst = [[1, 2], [3, 4], [5, 6], [7, 8]]
#Debe dar de salida lst2= [1, 2, 3, 4, 5, 6, 7, 8]

#lst2 = sum(lst, [])
#print(lst2)

#Opcion con ciclos
#lst_resultado = []
#for elem in lst:
#    for num in elem:
#        lst_resultado.append(num)
        
#print(lst_resultado)

#EJERCICIO 2
#Encontrar el numero mayor y el numero menor
#lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#menor = lst[0]
#mayor = lst[0]
#for elem in lst:
#    if elem > mayor:
#        mayor = elem
#    if elem < menor:
#        menor = elem
#print("Numero mayor ", mayor)
#print("Numero menor ", menor)
    
    
#Funciones

#Crear una funcion que al ingresar una lista con n radios de circulos retorne las n areas

#import math
#
#def area(radios):
#    areas = []
#    for radio in radios:
#        area = math.pi * (radio ** 2) 
#        areas.append(area)
#    return areas

#radios = [1, 2, 3, 4]
#areas = area(radios)
#print(areas)

#Crear una funcion que dada una string retorne la cantidad de vocales que hay en ella

#def vocales(string):
#    vocales = "aeiouAEIOU"
#    i = 0
#    for letra in string:
#        if letra in vocales:
#            i += 1
#    return i
#
#texto = "Camatachuqui"
#print(vocales(texto))

#Crear una funcion que dado un numero returne true si es primo o false si no es primo

# print(primo())
 
# def primo():
#     numero = int(input("Ingrese un numero: "))
#     if numero <= 1:
#         return False  
#     if numero == 2:
#         return True 
#     if numero % 2 == 0:
#         return False
#     for divisor in range(3, int(numero**0.5) + 1, 2):
#         if numero % divisor == 0:
#             return False


#print(primo())

def lista_primos(numeros):
    resultados = []
    for num in numeros:
        if num <= 1:
            resultados.append(False)
        elif num == 2:
            resultados.append(True)
        elif num % 2 == 0:
            resultados.append(False)
        else:
            es_primo = True
            for divisor in range(3, int(num**0.5) + 1, 2):
                if num % divisor == 0:
                    es_primo = False
                    break
            resultados.append(es_primo)
    return resultados


numeros = [1, 2, 3, 4, 5, 10, 13]
print(lista_primos(numeros))  

