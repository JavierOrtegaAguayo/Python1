# class Person:
#     def __init__(self, name, age, job, area):
#         self.name = name
#         self.age = age
#         self.job = job
#         self.area = area
        
#     def greet(self):
#         print(f"Hola soy {self.name}, tengo {self.age}, soy {self.job} y trabajo en {self.area}")
        
    
# persona1 = Person("Hugo", "23", "Ingeniero", "Tronadura")
# persona1.greet()

# class Machine:
#     def __init__(self, type, model, performance):
#         self.type = type
#         self.model = model
#         self.performance = performance
#         return
    
#     def presentation(self):
#         print(f"Tipo: {self.type}\n Modelo:{self.model}\n Rendiemiento: {self.performance}")
#         return
    
#     def fuel(self, distance):
#         self.liters = distance/self.performance
#         print(f"Para avanzar {distance} km, necesitamos {self.liters} litros de combustible")
#         return
        
        
# camion1 = Machine(type = "Camion", model = "CAT", performance = 0.2)
# camion1.presentation()
# camion1.fuel(100)

# class Rock:
#     def __init__(self, rocktype, density, grade):
#         self.rocktype = rocktype
#         self.density = density
#         self.grade = grade
    
#     def value(self, volume, price, recovery, cost):
#         block_tonnage = volume * self.density
#         earnings = block_tonnage * price * (recovery / 100) * (self.grade / 100) * 2004.6
#         losses = block_tonnage * cost
#         block_value = earnings - losses
#         print(f"El valor del bloque es {block_value}")
#         return
    
# roca1 = Rock(
#     rocktype = "Calcopirita",
#     density = 2.78,
#     grade = 0.9    
# )

# roca1.value(
#     volume = 1000,
#     price = 4,
#     recovery = 87,
#     cost = 5
# )

# A la clase de personas agregarle un atributo que sea sueldo,
# Agregar un metodo que diga "Soy nombre y gano sueldo"
# Agregar un metodo que si la persona es mayor a 30, duplicar el sueldo

class Person:
    def __init__(self, name, age, job, area, income):
        self.name = name
        self.age = age
        self.job = job
        self.area = area
        self.income = income
        
    def greet(self):
        print(f"Hola soy {self.name}, tengo {self.age}, soy {self.job} y trabajo en {self.area}")
    
    def earnings(self):
        print(f"Hola soy {self.name} y gano ${self.income}")
    
    def thirty(self):
        if int(self.age) > 30: 
            self.income *= 2
            print(f"Tengo mas de 30 años y gano ${self.income}")
        return
    
persona1 = Person("Hugo", "34", "Ingeniero", "Tronadura", 2000000)
persona1.greet()
persona1.earnings()
persona1.thirty()