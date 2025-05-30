import tkinter as tk

# Creamos una clase que se comporta como una ventana

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_variables()
        self.window_settings()
        
        self.widgets_create()
        self.widgets_layout()
        
    def window_variables(self):
        self.win_width = 800
        self.win_height = 600
        self.var_radios = tk.StringVar(value = "Cielo")
        return
    
    def window_settings(self):
        self.title("Mi ventana")
        self.geometry(f"{self.win_width}x{self.win_height}")
        self.resizable(False, False)
        return
    
    def widgets_create(self):
        self.label_tittle = tk.Label(self, text = "Radiobuttons", font = ("Arial", 20))   
        self.frame_radios = tk.Frame(self)
        self.radio_openpit = tk.Radiobutton(self.frame_radios, text = "Cielo abierto", value = "Cielo", variable = self.var_radios, command = self.selected_radio)
        self.radio_subte = tk.Radiobutton(self.frame_radios, text = "Subterranea", value = "Subte", variable = self.var_radios, command = self.selected_radio)  
        
        self.label_result = tk.Label(self, text = "") 
        return
    
    def widgets_layout(self):
        self.label_tittle.pack(pady = 15)
        self.frame_radios.pack()
        self.radio_openpit.pack()
        self.radio_subte.pack()
        
        self.label_result.pack(pady = 10)
        return
    
    def selected_radio(self):
        self.click = self.var_radios.get()
        if self.click == "Cielo":
            self.label_result.config(text = f"Has seleccionado Cielo")
        if self.click == "Subte":
            self.label_result.config(text = f"Has seleccionado Subterranea")
        
        return
    
if __name__ == "__main__":
    win = MainWindow()
    win.mainloop()