# import tkinter as tk
# from tkinter import ttk

# # Crear variables globales
# count = 1

# def add_rows():
#     global count
    
#     name = f"Person {count}"
#     age = str(20 + count)
#     tree.insert("", "end", values = (name, age))
#     count += 1
#     return

# # Creamos nuestra ventana
# root = tk.Tk()

# # Parametros de la ventana
# root.title("Ejemplo Tkinter")
# root.geometry("800x600")
# root.resizable(False,False)

# # Creamos los widgets
# # my_button = tk.Button(root, text = "Presiona")
# frame_tree = tk.Frame(root)
# scrollbar_tree = ttk.Scrollbar(frame_tree, orient = "vertical")
# tree = ttk.Treeview(frame_tree, columns = ("Nombre", "Edad"), show = "headings", yscrollcommand = scrollbar_tree.set) 

# # Colocamos los widgets
# frame_tree.pack()

# scrollbar_tree.pack(side = "right", fill = "y")
# tree.pack(side = "left", expand = "True", fill = "both")
# scrollbar_tree.config(command = tree.yview)

# button_rows = tk.Button(root, text = "Añadir filas", command = add_rows)

# button_rows.pack(pady = 20)
# # my_button.pack()
# # my_button.grid()
# # my_button.place()

# # Mainloop de la ventana
# root.mainloop()

import tkinter as tk
import pandas as pd
from tkinter import ttk, filedialog, messagebox

#Variables globales
df = None

def open_file():
    global df
    file_path = filedialog.askopenfilename(title = "Abrir archivo")
    if file_path:
        df = pd.read_csv(file_path, sep = ";")
        messagebox.showinfo("Archivo cargado", "Se ha cargado el archivo correctamente")
        after_read()
    return

def after_read():
    global combo_size_x, combo_size_y, combo_size_z
    
    combo_values = df.columns.tolist()
    
    combo_size_x["values"] = combo_values
    combo_size_y["values"] = combo_values
    combo_size_z["values"] = combo_values
    
    combo_size_x.config(state = "readonly")
    combo_size_y.config(state = "readonly")
    combo_size_z.config(state = "readonly")
    
    return
    
# Creamos nuestra ventana
root = tk.Tk()

# Parametros de la ventana
root.title("Ejemplo Tkinter 2")
root.geometry("800x600")
root.resizable(False,False)

# Creamos los widgets
my_button = tk.Button(root, text = "Abrir archivo", command = open_file)
frame_combo = tk.Frame(root)
combo_size_x = ttk.Combobox(frame_combo, state = "disabled")
label_size_x = tk.Label(frame_combo, text = "Tamaño x")

combo_size_y = ttk.Combobox(frame_combo, state = "disabled")
label_size_y = tk.Label(frame_combo, text = "Tamaño y")

combo_size_z = ttk.Combobox(frame_combo, state = "disabled")
label_size_z = tk.Label(frame_combo, text = "Tamaño z")

# Colocamos los widgets
my_button.pack(pady = 10)

frame_combo.pack(pady = 20)

combo_size_x.grid(row = 0, column = 0, pady = 5)
label_size_x.grid(row = 0, column = 1, pady = 5)

combo_size_y.grid(row = 1, column = 0, pady = 5)
label_size_y.grid(row = 1, column = 1, pady = 5)

combo_size_z.grid(row = 2, column = 0, pady = 5)
label_size_z.grid(row = 2, column = 1, pady = 5)

# Crear barra de menu
menubar = tk.Menu(root,)

menubar_file = tk.Menu(menubar, tearoff = 0)
menubar_file.add_command(label = "Abrir archivo", command = open_file)


menubar.add_cascade(label = "Archivo", menu = menubar_file)

root.config(menu = menubar)

# Mainloop de la ventana
root.mainloop()