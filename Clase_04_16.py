import numpy as np
#CREAR ARRAYS

# a = np.array([1, 2, 3])              #Array 1D
# b = np.array([[1, 2], [3, 4]])       #Array 2D
# c = np.zeros((2, 3))                 #2 filas 3 columnas
# d = np.ones((3, 3))
# e = np.eye(3)
# f = np.arange(0, 10, 2)
# g = np.linspace(0, 1, 5)             #5 valores entre 0 y 1

# print(g)

# #Propiedades de los array
# a.shape         #Tamaño
# a.dtype         #Tipo de dato
# a.ndim          #Dimension
# a.size          #Numero total de elementos

# #Operaciones
# x = np.array([1, 2, 3])
# y = np.array([4, 5, 6])

# x + y #[5, 6, 7]
# x * y #[4, 10, 18]
# x.mean()        #Media
# x.std()         #Desviacion estandar
# x.sum()         #Suma total

# #Indexacion
#a = np.array([[1, 2, 3], [4, 5, 6]])
# a[0, 1]          #2
# a[:, 1]          #Sagunda columna
# a[1, :]          #Segunda fila

#print(a[1, :])

#EJEMPLO
#DISTRIBUCION NORMAL
# mu, sigma = 0, 0.1
# samples = np.random.normal(mu, sigma, 1000)
# print(samples)

# import matplotlib as plt
# counts, bins, ignored = plt.hist(samples, 30, density = True)
# plt.plot(bins, 1/sigma)

import pandas as pd

# data = np.array([[1, 2], [3, 4], [5, 6]])
# df = pd.DataFrame(data, columns= ["A", "B"])
# print(data)
# print(df)

# df = pd.DataFrame({
#     "Altura (cm)" : np.random.normal(170, 10, 100),
#     "Peso (kg)" : np.random.normal(65, 15, 100)
# })

# media_altura = df["Altura (cm)"].mean()
# print(media_altura)



#EJEMPLO 
#Filtrar el modelo en x/2 +/- 200 [m], y/2 +/- 200 [m], z <= 3500
#Realizar un analisis descriptivo de la ley
#Crear ley random con estadisticas parecidad, crear columna ley 2

import pandas as pd
df = pd.read_csv("data.txt", sep= "\t")
#print(df.describe())
#FILTRAMOS POR LA MEDIANA
df = df[df["x"] <=24325 + 200]
df = df[df["x"] >=24325 - 200]
df = df[df["y"] <=25175 + 200]
df = df[df["y"] <=25175 -200]
df = df[df["z"] <= 3500]


media = df['ley'].mean()
desviacion = df['ley'].std()
tamaño = len(df)

#CREAR COLUMNA DE LEY ARTIFICIAL
df['ley2'] = np.random.normal(loc=media, scale=desviacion, size=tamaño)
#print(df.describe())

#Crear condicion de lo que sea negativo se vaya a 0

#Cuando calculemos la ley de corte dependiendo de los precios y los costos, esa ley de corte state

precio_cu = 4.5
costo_ryv = 1
den = 2.7
ton = 10 * 10 * 10 * den
costo_mina = 18
costo_planta = 19
recuperacion = 0.85
constante = 2204.62

#CALCULAR EL VALOR DE CADA BLOQUE
#AGREGAR NUEVA COLUMNA
df["Valor_bloque"] = ton * ((precio_cu - costo_ryv) * df["ley"] / 100) * recuperacion * constante - ton * (costo_mina + costo_planta)
#print(df.head())
#print(df.describe())


df["State"] = 0
for index, row in df.iterrows():
    if row["Valor_bloque"] >= 0:
        df.at[index, "State"] = 1
        
#print(df.describe())

#print(df["State"].value_counts())

#Envolvente economica, que volumen de tonelaje voy a extraer, cuales bloques son factibles de extraer
print(df.head())