import sys
import os

# Add the directory of the current script to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import bpy
from cube import Cube

def create_cube():
    Cube(0, 0, 0, 10)
    bpy.ops.wm.save_mainfile()

if __name__ == "__main__":
    create_cube()