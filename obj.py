import bpy
import random


class Obj:
    """Object / Mesh / Thing"""

    def __init__(
        self,
        mesh_type: str,
        material: str,
        size: list[int] = [1, 1, 1],
        pos: list[int] = [0, 0, 0, 0],
        rot: list[int] = [0, 0, 0],
    ):
        """
        Init Obj

        Args:
            mesh_type (str): Cube, Plane etc.
            material (str): The name of a pre-created material
            size: (list): x, y, z-axis size
            pos (list): x, y, z-axis & z-extra position
            rot (list): x, y, z-axis rotation
        """
        self.mesh_type = self._create_obj(mesh_type)
        self.obj = bpy.context.object
        self.material = self.set_material(material)

        self.size = self.set_scale(size[0], size[1], size[2])
        self.pos = self.set_position(pos[0], pos[1], pos[2], pos[3])
        self.rotation = self.set_rotation(rot[0], rot[1], rot[2])

    def _create_obj(self, mesh_type: str):
        """
        Creates an object

        Args:
            mesh_type (str): Cube, Plane etc.
        """
        match mesh_type:
            case "Cube":
                bpy.ops.mesh.primitive_cube_add()
            case "Ellipse":
                bpy.ops.curve.primitive_ellipse_add()
            case "Sphere":
                bpy.ops.mesh.primitive_uv_sphere_add()
            case "Cylinder":
                bpy.ops.mesh.primitive_cylinder_add()
            case "Code":
                bpy.ops.mesh.primitive_cone_add()
            case "Torus":
                bpy.ops.mesh.primitive_torus_add()
            case "Plane":
                bpy.ops.mesh.primitive_plane_add()
            case "Circle":
                bpy.ops.curve.primitive_circle_add()
            case _:
                bpy.ops.mesh.primitive_cube_add()

    def set_scale(self, x: int, y: int, z: int):
        """
        Sets size of object

        Args:
            x (int): x-axis scale
            y (int): y-axis scale
            z (int): z-axis scale
        """
        self.obj.scale.x = x
        self.obj.scale.y = y
        self.obj.scale.z = z

    def set_position(self, x: int, y: int, z: int, z_extra: None):
        """
        Sets position of object

        Args:
            x (int): x-axis position
            y (int): y-axis position
            z (int): z-axis position
        """
        self.obj.location.x = x
        self.obj.location.y = y

        # Calculate half z scale as default
        if z_extra == None:
            self.obj.location.z = self.obj.scale.z
        # Otherwise z scale + z_extra
        else:
            self.obj.location.z = self.obj.scale.z + z_extra

    def set_rotation(self, x: int, y: int, z: int):
        """
        Sets rotation of object

        Args:
            x (int): x-axis rotation
            y (int): y-axis rotation
            z (int): z-axis rotation
        """
        bpy.context.active_object.rotation_mode = "XYZ"
        bpy.context.active_object.rotation_euler = (x, y, z)

    def set_random_scale(self, min: int, max: int):
        """
        Sets random scale of object

        Args:
            min (int): min axis scale
            max (int): max axis scale
        """
        rx = random.uniform(min, max)
        ry = random.uniform(min, max)
        rz = random.uniform(min, max)

        self.obj.scale.x = rx
        self.obj.scale.y = ry
        self.obj.scale.z = rz

    def set_color(self, color: str):
        """
        Sets color of object

        Args:
            color (str): hex-value of the color
        """
        material = bpy.data.materials.new("Material")
        material.use_nodes = True
        principled = material.node_tree.nodes["Principled BSDF"]
        principled.inputs["Base Color"].default_value = self.hex_to_rgb(color)

        self.obj.data.materials.append(material)

    def set_material(self, material_name: str):
        """
        Sets material of object

        Args:
            material_name (str): name of pre-created material
        """
        material = bpy.data.materials.get(material_name)

        if self.obj.data.materials:
            self.obj.data.materials[0] = material
        else:
            self.obj.data.materials.append(material)

    def set_random_color_from_list(self, colors: list[str] = []):
        """
        Sets random color to object (from a list)

        Args:
            colors (list): a list of hex-values
        """
        material = bpy.data.materials.new("Material")
        material.use_nodes = True
        principled = material.node_tree.nodes["Principled BSDF"]

        principled.inputs["Base Color"].default_value = self._hex_to_rgba(
            random.choice(colors)
        )
        self.obj.data.materials.append(material)

    def _hex_to_rgba(value: str):
        """
        Converts hex to rgba

        Args:
            value (list): a hex-value
        """
        gamma = 2.2
        value = value.lstrip("#")
        lv = len(value)
        fin = list(int(value[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))
        r = pow(fin[0] / 255, gamma)
        g = pow(fin[1] / 255, gamma)
        b = pow(fin[2] / 255, gamma)
        fin.clear()
        fin.append(r)
        fin.append(g)
        fin.append(b)
        fin.append(1.0)
        return tuple(fin)
