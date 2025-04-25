import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('database.txt', sep=' ')
# print(df)

# ejex = df["X"]
# ejey = df["Y"]
# etiquetas = ["Linea"]

# plt.scatter(ejex,ejey, label = etiquetas)
# plt.xlabel("Eje x")
# plt.ylabel("Eje y")
# plt.title("Mi primer grafico en Matplotlib")
# plt.legend()

# # Mostrar el grafico
# plt.show()



# df2 = pd.read_csv('modelo2.txt', sep='\t')
# datos = df2["CUT"]

# plt.hist(datos, bins = 8, color = "red", edgecolor = "black")

# plt.xlabel("Ley de cobre (%)")
# plt.ylabel("Frecuencia")
# plt.title("Histograma de ley de cobre")

# plt.show()



# 1 fila y 2 columnas
fig, ax = plt.subplots(1, 2)

ax[0].plot([8, 15, 12, 21], [3, 4, 7, 1])
ax[0].set_title("Grafico 1")

ax[1].bar([10, 14, 4, 9, 2], [22, 13, 6, 0, 5])
ax[1].set_title("Grafico 2")

plt.tight_layout()
plt.show()

