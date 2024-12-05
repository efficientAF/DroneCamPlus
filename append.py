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
    bl_label = "Add Drone"
    
    def execute(self, context):
        import os  # Ensure you have the import
        import bpy  # Ensure Blender's module is available
        
        # Get the path to the current addon folder
        addon_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the path to the blend file
        blend_file_path = os.path.join(addon_dir, "blend", "DroneCam.blend")
        
        # Ensure the file exists
        if not os.path.isfile(blend_file_path):
            self.report({'ERROR'}, f"Blend file not found: {blend_file_path}")
            return {'CANCELLED'}

        collection_name = "DroneCam"

        with bpy.data.libraries.load(blend_file_path, link=False) as (data_from, data_to):
            # Check if the desired collection exists in the blend file
            if collection_name in data_from.collections:
                data_to.collections = [collection_name]
            else:
                self.report({'ERROR'}, f"Collection '{collection_name}' not found in {blend_file_path}")
                return {'CANCELLED'}

        # Append the collection to the current scene
        for collection in data_to.collections:
            if collection.name == collection_name:
                bpy.context.scene.collection.children.link(collection)
                self.report({'INFO'}, f"'{collection_name}' has been added to the current scene.")
                return {'FINISHED'}

        self.report({'ERROR'}, f"Failed to append '{collection_name}'.")
        return {'CANCELLED'}



def register_append(cls):
    # Modify the existing draw method to add keyframing buttons
    original_draw = cls.draw

    def modified_draw(self, context):

        # Add keyframing buttons
        layout = self.layout
        col = layout.column()
        row = col.row()
        row.scale_y = 3
        row.operator("object.append_dronecam")

        # Call the original draw method first
        original_draw(self, context)

    # Replace the draw method
    cls.draw = modified_draw

    # Register the operators
    bpy.utils.register_class(OBJECT_OT_AppendDroneCam)

def unregister_append(cls):
    # Unregister the operators
    bpy.utils.unregister_class(OBJECT_OT_AppendDroneCam)