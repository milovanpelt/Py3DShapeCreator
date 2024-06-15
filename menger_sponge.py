import sys
import os

# Add the directory of the current script to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from cube import Cube

class Menger_Sponge:
    def __init__(self, _x, _y, _z, _size):
        self.x = _x
        self.y = _y
        self.z = _z
        self.size = _size
        self.sponge = []
        startingCube = Cube(self.x, self.y, self.z, self.size)
        self.sponge.append(startingCube)

    def __CreateCubes(self, cube):
        cubes = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    new_size = cube.size / 3
                    new_x_position = cube.x + (x * new_size)
                    new_y_position = cube.y + (y * new_size)
                    new_z_position = cube.z + (z * new_size)
                    new_cube = Cube(new_x_position, new_y_position, new_z_position, new_size)
                    cubes.append(new_cube)
        return cubes
    
    def generate(self, iterations):
        for i in range(iterations):
            next_boxes = []
            for cube in self.sponge:
                new_boxes = self.__CreateCubes(cube)
                next_boxes.extend(new_boxes)
            self.sponge = next_boxes