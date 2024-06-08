import tkinter as tk

class ShapeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x300")
        self.window.title("Shape Creator")

        button = tk.Button(self.window, text="Create Shape", font=('Arial', 18), command=self.CreateBlenderCube)
        button.pack(padx=10, pady=10)

        self.window.mainloop()

    def CreateBlenderCube(self):
        print("Created Blender Cube")

ShapeGUI()