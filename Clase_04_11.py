import pandas as pd
data = {
    "Nombre" : ["Ana", "Luis", "Pedro", "Carla", "Jorge", "Lucia", "Andres", "Sofia", "Marcos", "Valeria"],
    "Edad" : [15, 30, 17, 22, 35, 8, 24, 26, 31, 2],
    "Pais" : ["España", "Mexico", "Chile", "Colombia", "Argentina", "Peru", "Uruguay", "Ecuador", "Bolivia", "Paraguay"]
}


df = pd.DataFrame(data)
#CREAR COLUMNA CANTIDAD DE MESES
df["Meses"] = df["Edad"] * 12

#CREAR COLUMNA SI ES MAYOR O NO, CUIDADO ITERROWS NO ES VECTORIZADA
df["Adulto"] = 0
for index, row in df.iterrows():
    if row["Edad"] >= 18:
        df.at[index, "Adulto"] = 1

print(df)

#RECORRER DATOS
for index, row in df.iterrows():
    print(f"Persona {index + 1}")
    print(f"Soy {row["Nombre"]}, tengo {row["Edad"]} años y soy de {row["Pais"]} ")
    print(" ")
    
    
#IMPORTAR EL MODELO, ESTA SEPARADO POR INDENTACION O TABS
df2 = pd.read_table("modelo2.txt", sep = "\t", header = 0 )
print(df2)
#CREAR NUEVA COLUMAN DE TONELAJE
block_volume = 10 * 10 * 10
df2["TON"] = block_volume * df2["DENSITY"]

df2["CU_Q"] = (df2["CUT"]/100) * df2["TON"]
print(df2)

col_CUT = df2["CUT"].tolist()
print(col_CUT)

print(max(col_CUT))
print(df2.describe())

