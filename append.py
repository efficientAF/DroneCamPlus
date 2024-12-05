# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy, os

# Operator to append DroneCam
class OBJECT_OT_AppendDroneCam(bpy.types.Operator):
    bl_idname = "object.append_dronecam"
    bl_label = "Stop Recording"
    
    def execute(self, context):

        # Get the path to the current addon folder
        addon_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the path to the blend file
        blend_file_path = os.path.join(addon_dir, "blend", "DroneCam.blend")
        
        # Ensure the file exists
        if not os.path.isfile(blend_file_path):
            print(f"Blend file not found: {blend_file_path}")
            return

        collection_name = "DroneCam"

        with bpy.data.libraries.load(blend_file_path, link=False) as (data_from, data_to):
            # Check if the desired collection exists in the blend file
            if collection_name in data_from.collections:
                data_to.collections = [collection_name]
            else:
                print(f"Collection '{collection_name}' not found in {blend_file_path}")
                return

        # Append the collection to the current scene
        for collection in data_to.collections:
            if collection.name == collection_name:
                bpy.context.scene.collection.children.link(collection)
                print(f"'{collection_name}' has been added to the current scene.")
                return

        print(f"Failed to append '{collection_name}'.")

        return {'FINISHED'}


def register_append(cls):
    # Modify the existing draw method to add keyframing buttons
    original_draw = cls.draw

    def modified_draw(self, context):
        # Call the original draw method first
        original_draw(self, context)
        
        # Add keyframing buttons
        layout = self.layout
        col = layout.column()
        col.separator()
        col.label(text="Add DroneCam")
        row = col.row()
        row.operator("object.append_dronecam")

    # Replace the draw method
    cls.draw = modified_draw

    # Register the operators
    bpy.utils.register_class(OBJECT_OT_AppendDroneCam)

def unregister_keyframing(cls):
    # Unregister the operators
    bpy.utils.unregister_class(OBJECT_OT_AppendDroneCam)