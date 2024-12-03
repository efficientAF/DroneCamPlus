import bpy

# Global dictionary to track the last recorded values
last_recorded_values = {
    "LeftThumbX": None,
    "LeftThumbY": None,
    "RightThumbX": None,
    "RightThumbY": None
}

# Flag to enable/disable keyframing
is_keyframing_active = False

def keyframe_xinput_properties(scene):
    # Only keyframe if the flag is active
    if not is_keyframing_active:
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
        "LeftThumbX", 
        "LeftThumbY", 
        "RightThumbX", 
        "RightThumbY"
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
                
            # Update the last recorded value
            last_recorded_values[prop] = current_value
                
            print(f"Keyframed {prop} at frame {current_frame}: {current_value}")
        
        except (KeyError, TypeError):
            print(f"Property {prop} not found in XInput Reader!")

# Operator to start keyframing
class OBJECT_OT_StartXInputKeyframing(bpy.types.Operator):
    bl_idname = "object.start_xinput_keyframing"
    bl_label = "Start Keyframing"
    
    def execute(self, context):
        global is_keyframing_active
        
        # Add the keyframing function to the frame change handler if not already there
        if keyframe_xinput_properties not in bpy.app.handlers.frame_change_pre:
            bpy.app.handlers.frame_change_pre.append(keyframe_xinput_properties)
        
        # Reset last recorded values
        for prop in last_recorded_values:
            last_recorded_values[prop] = None
        
        is_keyframing_active = True
        print("XInput Reader keyframing activated!")
        return {'FINISHED'}

# Operator to stop keyframing
class OBJECT_OT_StopXInputKeyframing(bpy.types.Operator):
    bl_idname = "object.stop_xinput_keyframing"
    bl_label = "Stop Keyframing"
    
    def execute(self, context):
        global is_keyframing_active
        is_keyframing_active = False
        print("XInput Reader keyframing stopped.")
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
        col.label(text="Keyframing")
        row = col.row()
        row.operator("object.start_xinput_keyframing")
        row.operator("object.stop_xinput_keyframing")

    # Replace the draw method
    cls.draw = modified_draw

    # Register the operators
    bpy.utils.register_class(OBJECT_OT_StartXInputKeyframing)
    bpy.utils.register_class(OBJECT_OT_StopXInputKeyframing)

def unregister_keyframing(cls):
    # Unregister the operators
    bpy.utils.unregister_class(OBJECT_OT_StartXInputKeyframing)
    bpy.utils.unregister_class(OBJECT_OT_StopXInputKeyframing)
    
    # Remove the keyframing handler if it's registered
    if keyframe_xinput_properties in bpy.app.handlers.frame_change_pre:
        bpy.app.handlers.frame_change_pre.remove(keyframe_xinput_properties)