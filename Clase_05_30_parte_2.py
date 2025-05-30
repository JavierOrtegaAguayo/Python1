import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.window_variables()
        self.window_settings()
        self.widgets_create()
        self.widgets_layout()
        return
    
    def window_variables(self):
        self.width = 800
        self.heigth = 600
        self.var_camion = tk.IntVar()
        self.var_pala = tk.IntVar()
        self.var_bulldozer = tk.IntVar()
        
        return
    
    def window_settings(self):
        self.title("Checkbuttons")
        self.geometry(f"{self.width}x{self.heigth}")
        self.resizable(False, False)
        return
    
    def widgets_create(self):
        self.label_title= tk.Label(self, text = "Checkbuttons")
        
        self.frame_check = tk.Frame(self)
        self.check_camion = tk.Checkbutton(self.frame_check, text = "Camion", variable = self.var_camion)
        self.check_pala = tk.Checkbutton(self.frame_check, text = "Pala", variable = self.var_pala)
        self.check_bulldozer = tk.Checkbutton(self.frame_check, text = "Bulldozer", variable = self.var_bulldozer)
        
        self.button_text = tk.Button(self, text = "Siguiente", command = self.selected_check)
        
        return
    
    def widgets_layout(self):
        self.label_title.pack(pady = 15)
        self.frame_check.pack()
        self.check_camion.pack()
        self.check_pala.pack()
        self.check_bulldozer.pack()
        self.button_text.pack()
        return
    
    def selected_check(self):
        selected = []
        if self.var_camion.get():
            selected.append("Camion")
        if self.var_pala.get():
            selected.append("Pala")
        if self.var_bulldozer.get():
            selected.append("Bulldozer")
            
        print(selected)
    
if __name__ == "__main__":
    win = App()
    win.mainloop()    
    