# Tarea 1 "PYTHON APLICADO A MINERÍA" Javier Ortega A. 2021444980

import pandas as pd
import plotly.express as px
import numpy as np
from scipy.stats import lognorm

# Cargamos el modelo de bloques

df = pd.read_csv('data.txt', sep='\t') 

# Visualizamos los primeros 5 datos
# print(df.head())

# Entrega 
#        x      y     z   ley
# 0  24105  24405  2755  0.55
# 1  24105  24405  2765  0.55
# 2  24105  24405  2775  0.55
# 3  24105  24405  2785  0.55
# 4  24105  24405  2795  0.55

# Estadistica descriptiva
# print(df.describe())

# # Entrega    x             y             z           ley
# count  1.048575e+06  1.048575e+06  1.048575e+06  1.048575e+06
# mean   2.432407e+04  2.517733e+04  3.499973e+03  4.145748e-01
# std    1.293551e+02  4.493572e+02  4.330033e+02  1.958465e-01
# min    2.410500e+04  2.440500e+04  2.755000e+03  1.000000e-02
# 25%    2.421500e+04  2.478500e+04  3.125000e+03  2.500000e-01
# 50%    2.432500e+04  2.517500e+04  3.495000e+03  4.200000e-01
# 75%    2.443500e+04  2.556500e+04  3.875000e+03  5.500000e-01
# max    2.454500e+04  2.595500e+04  4.245000e+03  2.580000e+00

# Graficar el histograma y boxplot de la variable ‘ley’

hist = px.histogram(df, x='ley', title='Histograma de ley')
hist.show()

box = px.box(df, y='ley', title='Boxplot de ley')
box.show()

# Media y desviación estándar de la ley original
media = df['ley'].mean()
std = df['ley'].std()

# Parámetros para la distribución lognormal
sigma = np.sqrt(np.log(1 + (std**2) / (media**2)))
mu = np.log(media) - 0.5 * sigma**2

# Generar ley2 con distribución lognormal
ley2 = lognorm.rvs(s=sigma, scale=np.exp(mu), size=len(df))

df['ley2'] = ley2
hist2 = px.histogram(df, x='ley2', title='Histograma de ley 2')
hist2.show()

# Crear una columna para cada variable de ley que valorice cada uno de los bloques de acuerdo a la ecuación (1).
precio_cu = 4.86
costo_ryv = 1
den = 2.7
ton = 10 * 10 * 10 * den
costo_mina = 18
costo_planta = 19
recuperacion = 0.85
constante = 2204.62

df["Valor_bloque"] = ton * ((precio_cu - costo_ryv) * df["ley"] / 100) * recuperacion * constante - ton * (costo_mina + costo_planta)
df["Valor_bloque2"] = ton * ((precio_cu - costo_ryv) * df["ley2"] / 100) * recuperacion * constante - ton * (costo_mina + costo_planta)


df['status_ley'] = (df['Valor_bloque'] > 0).astype(int)
df['status_ley2'] = (df['Valor_bloque2'] > 0).astype(int)


# Envolvente usando la ley original
fig1 = px.scatter_3d(df[df['status_ley'] == 1], 
                     x='x', 
                     y='y', 
                     z='z',
                     color='ley', 
                     title='Envolvente 3D (ley original)')
fig1.show()

# Envolvente usando la ley2
fig2 = px.scatter_3d(df[df['status_ley2'] == 1],
                     x='x',
                     y='y', 
                     z='z',
                     color='ley2',
                     title='Envolvente 3D (ley2)')
fig2.show()

# La envolvente usando la ley 2 obtenida de forma aleatoria no representa bien una envoelvente 
# economica ya que los valores de ley estan distribuidos uniformemente en todo el espacio,
# no contempla la distribucion espacial del mineral que existe en la vida real.
