import bpy


class Scene:
    """Scene"""

    def delete_all_objects_of_type(self, objs: list[str]):
        """
        Delete all objects by type

        Args:
            obj_type (str): The object type, cube, plane etc.
        """
        for obj in bpy.context.scene.objects:
            if any(obj.name.startswith(s.capitalize()) for s in objs):
                bpy.data.objects.remove(obj, do_unlink=True)

    def delete_all_materials_except(self, materials: list):
        """
        Deletes all materials except the ones in [materials]

        Args:
            materials ([str, str]): A list of material names
        """
        for material in bpy.data.materials:
            if material.name not in materials:
                material.user_clear()
                bpy.data.materials.remove(material)

    def set_world_color(self, color: str):
        """
        Sets project world color by hex value.

        Args:
            color (str): The hex value of the new color
        """
        bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[
            0
        ].default_value = self._hex_to_rgba(color)

    def _hex_to_rgba(self, hex_value: str):
        """
        Converts hex to rgb-color

        Args:
            hex_value (str): The colors' hex value

        Returns (tuple) the rgba value
        """
        gamma = 2.2
        hex_value = hex_value.lstrip("#")
        lv = len(hex_value)
        fin = list(int(hex_value[i : i + lv // 3], 16) for i in range(0, lv, lv // 3))
        r = pow(fin[0] / 255, gamma)
        g = pow(fin[1] / 255, gamma)
        b = pow(fin[2] / 255, gamma)
        fin.clear()
        fin.append(r)
        fin.append(g)
        fin.append(b)
        fin.append(1.0)
        return tuple(fin)

    def setup(self, del_objs: list[str], del_materials: list[str], world_color: str):
        """
        Temporary setup method for mini-projects

        Args:
            del_objs (list): objects (str) to be deleted on script run
            del_materials (list): materials (str) to be deleted on script run
            world_color (str): the color of the world
        """
        self.delete_all_objects_of_type(del_objs)
        self.delete_all_materials_except(del_materials)
        self.set_world_color(world_color)

    def save_as_png(self, file_name: str):
        """
        Save image as png

        Args:
            file_name (str): the name of the saved file
        """
        bpy.ops.image.save_as(
            save_as_render=True,
            copy=True,
            filepath=f"//..\\Desktop\\{file_name}.png",
            show_multiview=False,
            use_multiview=False,
        )
