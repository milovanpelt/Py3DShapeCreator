import bpy

class Cube:
    def __init__(self, x, y, z, _size):
        bpy.ops.mesh.primitive_cube_add(size=_size, enter_editmode=False, align='WORLD', location=(x, y, z))