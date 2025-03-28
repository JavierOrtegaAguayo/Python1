# mi_lista = [1, 2, "abc", [1, "a"]]
# mi_tupla = (1, "a", "b", "c")

# my_list = [27, 12, 9.8, "Perro", "Gato", [1, 2, 3]]

# elem = my_list[3]
#print(elem)

# for i in range(5):  # 0, 1, 2, 3, 4
#     print(i)

# for i in range(len(my_list)):
#    elem = my_list[i]
#    print(elem)
    
# my_list[2] = "Hola"

# my_list.append("Hola")

# print("Hola")

# Tuplas no se pueden modificar

#Ejercicio: Recorrer la lista y si hay un numero mayor o igual a 10 cambiarlo por otra cosa
# my_list = [10, 5, 4, 15, 2, 9, 20, 100]

# for i in range(len(my_list)):
#     if my_list[i] >= 10:
#         my_list[i] = "Hola"
        
# print(my_list)
        
# DICCIONARIOS
# keys, values, items

#dicc = {
#    "nombre" : "Felipe"
#    "edad" : 23
#    "universidad" : "Udec"
#}

#print(dicc["universidad"])

#rock_database = {
#    "nombre" : "diorita"
#    "RMR" : 90
#    "UCS" : 250
#}

#print(rock_database["UCS"])

rock_database = {
    "Diorita" : {
        "RMR" : 90,
        "UCS" : 250,
        "Dureza" : 10
    },
    "Andesita" : {
        "RMR" : 85,
        "UCS" : 150,
        "Dureza" : 9
    }
}

print(rock_database["Diorita"]["UCS"])