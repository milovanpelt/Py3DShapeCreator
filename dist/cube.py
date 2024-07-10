import bpy

class Cube:
    def __init__(self, _x, _y, _z, _size):
        self.x =_x
        self.y = _y
        self.z = _z
        self.size = _size
    
    def create(self):
        bpy.ops.mesh.primitive_cube_add(size=self.size, enter_editmode=False, align='WORLD', location=(self.x, self.y, self.z))