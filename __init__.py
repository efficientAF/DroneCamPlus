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

import bpy, os, sys, subprocess

import XInput

from bpy.types import (Operator, Panel, AddonPreferences)   

#--------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------PREFERENCES-----------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------#

class XR_PT_preferences_panel(AddonPreferences):
    bl_idname = __package__

    def draw(self, context):
        layout = self.layout

#------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------FUNCTIONS-----------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------#


def get_reader():
    return bpy.data.objects.get("XInput Reader")

def create_reader():
    xinput_reader_empty = bpy.data.objects.get("XInput Reader")
    if xinput_reader_empty is None:
        xinput_reader_empty = bpy.data.objects.new("XInput Reader", None)
        xinput_reader_empty.use_fake_user = True
        # bpy.context.scene.collection.objects.link(xinput_reader_empty)
    return xinput_reader_empty

# Flag to enable/disable keyframing
is_recording_active = False

def keyframe_xinput_properties(scene):
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



#------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------OPERATORS-----------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------#


class OBJECT_OT_AppendDroneCam(bpy.types.Operator):
    bl_idname = "object.append_dronecam"
    bl_label = "Add DroneCam"
    
    def execute(self, context):
        
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


class XR_OT_DroneCamStartStop(Operator):
    bl_idname = "wm.dronecamstartstop"
    bl_label = "Start/Stop"
    bl_description = "Start and Stop DroneCam recording gamepad inputs"
    bl_options = {'REGISTER'}

    _timer = None
    
    def modal(self, context, event):
        xinput_reader_empty = get_reader()

        if event.type in {'RIGHTMOUSE', 'ESC'}:
            self.cancel(context)
            xinput_reader_empty.location = xinput_reader_empty.location
            return {'CANCELLED'}
        
        #Controller inputs
        state = XInput.get_state(0)

        xinput_reader_empty["A"] = XInput.get_button_values(state)['A']
        xinput_reader_empty["B"] = XInput.get_button_values(state)['B']
        xinput_reader_empty["X"] = XInput.get_button_values(state)['X']
        xinput_reader_empty["Y"] = XInput.get_button_values(state)['Y']
        xinput_reader_empty["DPadUp"] = XInput.get_button_values(state)['DPAD_UP']
        xinput_reader_empty["DPadDown"] = XInput.get_button_values(state)['DPAD_DOWN']
        xinput_reader_empty["DPadLeft"] = XInput.get_button_values(state)['DPAD_LEFT']
        xinput_reader_empty["DPadRight"] = XInput.get_button_values(state)['DPAD_RIGHT']
        xinput_reader_empty["Start"] = XInput.get_button_values(state)['START']
        xinput_reader_empty["Back"] = XInput.get_button_values(state)['BACK']
        xinput_reader_empty["LeftThumb"] = XInput.get_button_values(state)['LEFT_THUMB']
        xinput_reader_empty["LeftThumbX"] = XInput.get_thumb_values(state)[0][0]
        xinput_reader_empty["LeftThumbY"] = XInput.get_thumb_values(state)[0][1]
        xinput_reader_empty["RightThumb"] = XInput.get_button_values(state)['RIGHT_THUMB']
        xinput_reader_empty["RightThumbX"] = XInput.get_thumb_values(state)[1][0]
        xinput_reader_empty["RightThumbY"] = XInput.get_thumb_values(state)[1][1]
        xinput_reader_empty["LeftShoulder"] = XInput.get_button_values(state)['LEFT_SHOULDER']
        xinput_reader_empty["RightShoulder"] = XInput.get_button_values(state)['RIGHT_SHOULDER']
        xinput_reader_empty["LeftTrigger"] = XInput.get_trigger_values(state)[0]
        xinput_reader_empty["RightTrigger"] = XInput.get_trigger_values(state)[1]
        
        # trigger scene update
        xinput_reader_empty.location = xinput_reader_empty.location
        return {'PASS_THROUGH'}
    
    def execute(self, context):
        
        xinput_reader_empty = create_reader()

        global is_recording_active
        
        # Add the keyframing function to the frame change handler if not already there
        if keyframe_xinput_properties not in bpy.app.handlers.frame_change_pre:
            bpy.app.handlers.frame_change_pre.append(keyframe_xinput_properties)
        
        is_recording_active = True
        bpy.ops.screen.animation_play()
        
        print("DroneCam recording activated!")

        wm = context.window_manager
        self._timer = wm.event_timer_add(0.1, window=context.window)
        wm.modal_handler_add(self)
        

        wm.modal_running = True
        return {'RUNNING_MODAL'}
    
    def cancel(self, context):
        
        global is_recording_active
        is_recording_active = False

        # Stop animation playback if it is running
        if bpy.context.screen.is_animation_playing:
            bpy.ops.screen.animation_play()  # This stops playback
        

        print("DroneCam recording stopped.")

        wm = context.window_manager
        wm.event_timer_remove(self._timer)
        wm.modal_running = False
 

#------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------PANELS------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------------#


class XR_PT_panel(Panel):
    bl_label = "DroneCam"
    bl_idname = "OBJECT_PT_DroneCam_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "DroneCam"

    def draw(self, context):
        layout = self.layout
        col = layout.column()
        row = col.row()
        row.scale_y = 3
        row.operator("object.append_dronecam")
        if bpy.context.window_manager.modal_running == False:
            row.operator("wm.dronecamstartstop")
        else:
            row.operator("wm.dronecamstartstop", text="Right Click or Esc to Stop", icon="ERROR")
        col.separator()

        xinput_reader_empty = get_reader()
        if xinput_reader_empty is not None:
            controller_inputs = xinput_reader_empty.items()

            box = layout.box()
            box.label(text="Controller Inputs")
            param_count = 0
            for controller_input in controller_inputs:
                if type(xinput_reader_empty[controller_input[0]]) == float or int or bool:
                    row = box.row()
                    prop_name = controller_input[0]
                    row.prop(xinput_reader_empty, f'["{prop_name}"]')
                    param_count += 1

#--------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------REGISTER------------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------#


classes = (
    OBJECT_OT_AppendDroneCam,
    XR_OT_DroneCamStartStop,
    XR_PT_panel,
    XR_PT_preferences_panel,
)

def register():
    bpy.types.WindowManager.modal_running = bpy.props.BoolProperty(default=False)

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

def unregister():
    del bpy.types.WindowManager.modal_running

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)
