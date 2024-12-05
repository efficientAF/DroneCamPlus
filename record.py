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

import bpy

# Flag to enable/disable keyframing
is_recording_active = False

# Properties to keyframe
properties = [
    "A",
    "B",
    "X",
    "Y",
    "DPadUp",
    "DPadDown",
    "DPadLeft",
    "DPadRight",
    "Start",
    "Back",
    "LeftThumb",
    "LeftThumbX",
    "LeftThumbY",
    "RightThumb",
    "RightThumbX",
    "RightThumbY",
    "LeftShoulder",
    "RightShoulder",
    "LeftTrigger",
    "RightTrigger"
]

def keyframe_xinput_properties(scene, properties):
    # Only keyframe if the flag is active
    if not is_recording_active:
        return
    
    # Get the XInput Reader object
    try:
        xinput_obj = bpy.data.objects["XInput Reader"]
    except KeyError:
        print("XInput Reader object not found!")
        return
    
    # Get the current frame
    current_frame = scene.frame_current
    
    # Keyframe each property
    for prop in properties:
        try:
            current_value = xinput_obj[prop]
            
            # Insert a keyframe for the property
            xinput_obj.keyframe_insert(
                data_path=f'["{prop}"]', 
                frame=current_frame
            )
                
            print(f"Keyframed {prop} at frame {current_frame}: {current_value}")
        
        except (KeyError, TypeError):
            print(f"Property {prop} not found in XInput Reader!")

# Operator to start keyframing
class OBJECT_OT_StartRecording(bpy.types.Operator):
    bl_idname = "object.start_recording"
    bl_label = "Start Recording"
    
    def execute(self, context):
        global is_recording_active
        
        # Add the keyframing function to the frame change handler if not already there
        if keyframe_xinput_properties not in bpy.app.handlers.frame_change_pre:
            bpy.app.handlers.frame_change_pre.append(keyframe_xinput_properties)

        # Get the XInput Reader object
        try:
            xinput_obj = bpy.data.objects["XInput Reader"]
        except KeyError:
            print("XInput Reader object not found!")
            return

        try:
            xinput_obj.animation_data_clear()
        except AttributeError:
            print("Could not clear recording data")
            return
        
        is_recording_active = True
        bpy.ops.screen.animation_play()
        
        print("DroneCam recording activated!")
        return {'FINISHED'}

# Operator to stop keyframing
class OBJECT_OT_StopRecording(bpy.types.Operator):
    bl_idname = "object.stop_recording"
    bl_label = "Stop Recording"
    
    def execute(self, context):
        global is_recording_active
        is_recording_active = False

        if bpy.context.screen.is_animation_playing:
            bpy.ops.screen.animation_play()  # This stops playback

        print("DroneCam recording stopped.")
        return {'FINISHED'}

def register_keyframing(cls):
    # Modify the existing draw method to add keyframing buttons
    original_draw = cls.draw

    def modified_draw(self, context):
        # Call the original draw method first
        original_draw(self, context)
        
        # Add keyframing buttons
        layout = self.layout
        col = layout.column()
        col.separator()
        col.label(text="Recording")
        row = col.row()
        row.operator("object.start_recording")
        row.operator("object.stop_recording")

    # Replace the draw method
    cls.draw = modified_draw

    # Register the operators
    bpy.utils.register_class(OBJECT_OT_StartRecording)
    bpy.utils.register_class(OBJECT_OT_StopRecording)

def unregister_keyframing(cls):
    # Unregister the operators
    bpy.utils.unregister_class(OBJECT_OT_StartRecording)
    bpy.utils.unregister_class(OBJECT_OT_StopRecording)
    
    # Remove the keyframing handler if it's registered
    if keyframe_xinput_properties in bpy.app.handlers.frame_change_pre:
        bpy.app.handlers.frame_change_pre.remove(keyframe_xinput_properties)