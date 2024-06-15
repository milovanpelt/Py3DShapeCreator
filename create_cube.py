import bpy

def create_cube():
    bpy.ops.mesh.primitive_cube_add(size=10, enter_editmode=False, align='WORLD', location=(0,0,0))  

if __name__ == "__main__":
    create_cube()