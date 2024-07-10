import tkinter as tk
import subprocess
import os

class ShapeGUI:
    def __init__(self):
        # blender
        self.blender_executable_path = "C:/Program Files/Blender Foundation/Blender 4.1/blender.exe"
        self.blender_project_path = "C:/Users/Xonar/Documents/GitHub/Py3DShapeCreator/blender_menger_sponge.blend"
        self.shape_cube_script = os.path.join(os.getcwd(), 'create_cube.py')
        self.shape_menger_sponge_script = os.path.join(os.getcwd(), 'create_menger_sponge.py')

        # tk window
        self.window = tk.Tk()
        self.window.geometry("500x300")
        self.window.title("Shape Creator")

        blender_cube_creation_button = tk.Button(self.window, text="Create Cube", font=('Arial', 18), command=self.create_blender_cube)
        blender_cube_creation_button.pack(padx=10, pady=10)

        blender_sponge_creation_button = tk.Button(self.window, text="Create Menger Sponge", font=('Arial', 18), command=self.create_menger_sponge)
        blender_sponge_creation_button.pack(padx=10, pady=10)

        self.window.mainloop()
    def create_blender_cube(self):
        subprocess.run([self.blender_executable_path, self.blender_project_path, '--python', self.shape_cube_script])

    def create_menger_sponge(self):
        subprocess.run([self.blender_executable_path, self.blender_project_path, '--python', self.shape_menger_sponge_script])