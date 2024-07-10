import tkinter as tk
import subprocess
import os
from tkinter import filedialog

class ShapeGUI:
    def __init__(self):
        # blender
        #self.blender_executable_path = "C:/Program Files/Blender Foundation/Blender 4.1/blender.exe"
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

        # choosing executable file
        self.select_blender_exec_button = tk.Button(self.window, text="Select Blender Executable", command=self.select_blender_exec_file)
        self.select_blender_exec_button.pack(pady=10)

        self.path_blender_exec_label = tk.Label(self.window, text="No file selected")
        self.path_blender_exec_label.pack(pady=5)

        self.blender_executable_path = None

        # choosing project file
        self.select_blender_project_button = tk.Button(self.window, text="Select Blender Project File", command=self.select_blender_project_file)
        self.select_blender_project_button.pack(pady=10)

        self.path_blender_project_label = tk.Label(self.window, text="No file selected")
        self.path_blender_project_label.pack(pady=5)

        self.blender_project_path = None

        self.window.mainloop()

    def select_blender_exec_file(self):
    # Open a file dialog to select the Blender executable
        self.blender_executable_path = filedialog.askopenfilename(
            title="Select Blender Executable",
            filetypes=[("Executables", "*.exe")]
        )
        if self.blender_executable_path:
            # Update the label to show the selected path
            self.path_blender_exec_label.config(text=self.blender_executable_path)

    def select_blender_project_file(self):
    # Open a file dialog to select the Blender executable
        self.blender_project_path = filedialog.askopenfilename(
            title="Select Blender Project File",
            filetypes=[("Blender Files", "*.blend")]
        )
        if self.blender_project_path:
            # Update the label to show the selected path
            self.path_blender_project_label.config(text=self.blender_project_path)
            
    def create_blender_cube(self):
        subprocess.run([self.blender_executable_path, self.blender_project_path, '--python', self.shape_cube_script])

    def create_menger_sponge(self):
        subprocess.run([self.blender_executable_path, self.blender_project_path, '--python', self.shape_menger_sponge_script])