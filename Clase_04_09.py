#TRABAJANDO CON MODELOS DE BLOQUES
import pandas as pd
df = pd.read_csv("data.txt", sep= "\t")
df.head()
#FILTRAMOS CON LA MEDIANA
#SUMAMOS 100 METROS POR CADA LADO
df = df[df["x"] <=24325 + 100]
df = df[df["x"] >=24325 - 100]
df = df[df["y"] <=25175 + 100]
df = df[df["y"] >=25175 - 100]
#DE UN MILLON DE DATOS, PASAMOS A CERCA DE 66000

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
print(df.head())
print(df.describe())
#MAXIMO 7 MILLONES EN ALGUN BLOQUE


# Corrected code:
df["State"] = 0
for index, row in df.iterrows():
    if row["Valor_bloque"] >= 0:
        df.at[index, "State"] = 1
        
print(df.describe())

print(df["State"].value_counts())