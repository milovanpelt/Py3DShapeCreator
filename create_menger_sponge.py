import sys
import os

# Add the directory of the current script to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import bpy
from menger_sponge import Menger_Sponge

def create_menger_sponge():
    # save file after creation
    menger_sponge_first_iteration = Menger_Sponge(-7.5, 0, 0, 10)
    menger_sponge_first_iteration.generate(1)

    menger_sponge_second_iteration = Menger_Sponge(7.5, 0, 0, 10)
    menger_sponge_second_iteration.generate(2)

    # save file after creation
    bpy.ops.wm.save_mainfile()

if __name__ == "__main__":
    create_menger_sponge()