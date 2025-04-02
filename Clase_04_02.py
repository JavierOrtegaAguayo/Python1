# Manejo de cadenas
#texto = "Hola Mundo"
#print(texto.upper())
#print(type(texto))
#print(texto.lower())
#print(texto.split())

#? Comprensiones

#for x in range(10):
#    print(x)
    
#result = [x**2 for x in range(10)]
#print(result)

## Funcion lamda
#multiplicar = lambda x, y : x * y
#print(multiplicar)

#def filtrar_pares(lista_numeros):
#    pares = []
#    for num in lista_numeros:
#        if num % 2 == 0:
#            pares.append(num)
#    return pares
#
#print(filtrar_pares([1,2,3,4,5,6,7,8,9,10]))

#Contar veces que aparece una palabra
def contar_palabras(frase):
    palabras = frase.lower().split()  #Arroja lista de strings
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

#texto = input("Ingresa una oracion: ")
#print(contar_palabras(texto))

def mayores_de_edad(personas):   #Personas es una lista de tuplas
    nombres = []
    global x
    x = 5
    for nombre, edad in personas:
        if edad >= 18:
            nombres.append(nombre)
    return nombres

#datos = [("Ana", 25), ("Luis", 17), ("Carlos", 30), ("Marta", 19)]
#print(mayores_de_edad(datos))
#print(x)

import random 

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    while True:
        intento = int(input("Adivina el numero (1-100): "))
        intentos += 1
        if intento < numero_secreto:
            print("Mas alto")
        elif intento > numero_secreto:
            print("Mas bajo")
        else:
            print(f"Correcto, lo lograste en {intentos} intentos.")
            break

#adivina_el_numero()
        
#numero = random.gauss(0, 1)
#print(numero)

def gestor_tareas():
    tareas = []
    while True:
        print("\n --- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Completar tarea")
        print("3. Listar tarea")
        print("4. Salir")
        opcion = input("Elige una opcion: ")
        
        if opcion == "1":
            tarea = input("Describe la tarea: ")
            tareas.append({"tarea": tarea, "completada": False})
            print("Tarea agregada")
        elif opcion == "2":
            for i, tarea in enumerate(tareas):
                print(f"{i+1}.{tarea["tarea"]} ({Bien if tarea["completada"] else "Mal"})")
            num = int(input("Numero de tarea a completada.")) - 1
            tareas[num]["completada"] = True
            print("Tarea marcada como completada")
        elif opcion == "3":
            print("\n--- Tareas pendiente ---")
            for tarea in tareas:
                if not tarea["completada"]:
                    print(f"- {tarea["tarea"]} (Mal)")
        elif opcion == "4":
            break
        else:
            print("Opcion invalida")
            
#gestor_tareas()
import math
def perimetro_area():
    radio = float(input("Ingrese el radio: "))
    area = math.pi * radio**2
    perimetro = math.pi * 2 * radio
    print (f"El perimetro es: {perimetro}")
    print(f"El area es {area}")
    
perimetro_area()