import bpy
import os
import sys
import subprocess
import XInput

from . import ui
from . import RC_input
from bpy.props import EnumProperty, FloatProperty

# Global variables
is_recording_active = False

def get_reader():
    return bpy.data.objects.get("XInput Reader")

def create_reader():
    xinput_reader_empty = bpy.data.objects.get("XInput Reader")
    if xinput_reader_empty is None:
        xinput_reader_empty = bpy.data.objects.new("XInput Reader", None)
        xinput_reader_empty.use_fake_user = True
    return xinput_reader_empty

def keyframe_xinput_properties(scene):
    if not is_recording_active:
        return
    
    try:
        xinput_obj = bpy.data.objects["XInput Reader"]
    except KeyError:
        print("XInput Reader object not found!")
        return
    
    current_frame = scene.frame_current

    properties = [
        "LeftThumbX",
        "LeftThumbY",
        "RightThumbX",
        "RightThumbY"
    ]
    
    for prop in properties:
        try:
            current_value = xinput_obj[prop]
            xinput_obj.keyframe_insert(
                data_path=f'["{prop}"]', 
                frame=current_frame
            )
            print(f"Keyframed {prop} at frame {current_frame}: {current_value}")
        except (KeyError, TypeError):
            print(f"Property {prop} not found in XInput Reader!")

def get_input_values():
    """Get standardized input values regardless of source"""
    prefs = bpy.context.preferences.addons[__package__].preferences
    wm = bpy.context.window_manager
    input_type = "rc" if prefs.input_method == 'RC' else "xinput"
    
    if prefs.input_method == 'XINPUT':
        state = XInput.get_state(0)
        raw_values = {
            "Throttle": XInput.get_thumb_values(state)[0][1],
            "Yaw": XInput.get_thumb_values(state)[0][0],
            "Pitch": XInput.get_thumb_values(state)[1][1],
            "Roll": XInput.get_thumb_values(state)[1][0]
        }
    else:
        raw_values = RC_input.get_rc_input_values()
    
    # Apply sensitivity to values
    return {
        control: raw_values[control] * getattr(prefs, f"{input_type}_{control.lower()}_sensitivity")
        for control in raw_values
    }

class OBJECT_OT_AppendDroneCam(bpy.types.Operator):
    bl_idname = "object.append_dronecam"
    bl_label = "Add DroneCam"
    
    def execute(self, context):
        addon_dir = os.path.dirname(os.path.abspath(__file__))
        blend_file_path = os.path.join(addon_dir, "blend", "DroneCam.blend")
        
        if not os.path.isfile(blend_file_path):
            self.report({'ERROR'}, f"Blend file not found: {blend_file_path}")
            return {'CANCELLED'}

        collection_name = "DroneCam"

        with bpy.data.libraries.load(blend_file_path, link=False) as (data_from, data_to):
            if collection_name in data_from.collections:
                data_to.collections = [collection_name]
            else:
                self.report({'ERROR'}, f"Collection '{collection_name}' not found in {blend_file_path}")
                return {'CANCELLED'}

        for collection in data_to.collections:
            if collection.name == collection_name:
                bpy.context.scene.collection.children.link(collection)
                self.report({'INFO'}, f"'{collection_name}' has been added to the current scene.")
                return {'FINISHED'}

        self.report({'ERROR'}, f"Failed to append '{collection_name}'.")
        return {'CANCELLED'}

class XR_OT_DroneCamStartStop(bpy.types.Operator):
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
        
        # Use the abstraction layer
        values = get_input_values()
        
        # Map standardized values to the reader object
        xinput_reader_empty["LeftThumbX"] = values["Yaw"]
        xinput_reader_empty["LeftThumbY"] = values["Throttle"]
        xinput_reader_empty["RightThumbX"] = values["Roll"]
        xinput_reader_empty["RightThumbY"] = values["Pitch"]
        
        xinput_reader_empty.location = xinput_reader_empty.location
        return {'PASS_THROUGH'}
    
    def execute(self, context):
        xinput_reader_empty = create_reader()
        global is_recording_active
        
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

        if bpy.context.screen.is_animation_playing:
            bpy.ops.screen.animation_play()

        print("DroneCam recording stopped.")

        wm = context.window_manager
        wm.event_timer_remove(self._timer)
        wm.modal_running = False

class DRONECAM_OT_refresh_devices(bpy.types.Operator):
    bl_idname = "dronecam.refresh_devices"
    bl_label = "Refresh RC Devices"
    bl_description = "Scan for connected RC devices"
    
    def execute(self, context):
        from . import RC_input
        devices = RC_input.scan_for_rc_devices()
        count = len(devices)
        self.report({'INFO'}, f"Found {count} RC device{'s' if count != 1 else ''}")
        return {'FINISHED'}

class DRONECAM_OT_select_device(bpy.types.Operator):
    bl_idname = "dronecam.select_device"
    bl_label = "Select RC Device"
    
    device_name: bpy.props.StringProperty()
    device_path: bpy.props.StringProperty()
    
    def execute(self, context):
        prefs = context.preferences.addons[__package__].preferences
        prefs.selected_device = self.device_name
        return {'FINISHED'}

# Add timer callback
def update_rc_values():
    # Only update if preview is active
    prefs = bpy.context.preferences.addons[__package__].preferences
    if not prefs.rc_preview_active:
        return 0.1
        
    RC_input.update_channel_values()
    # Force UI update
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            area.tag_redraw()
    return 0.1  # Update every 0.1 seconds

def register_rate_props():
    # YPR Rate properties
    for control in ["Yaw", "Pitch", "Roll"]:
        setattr(bpy.types.WindowManager, f"rc_{control.lower()}_center",
            FloatProperty(
                name="Center Sensitivity",
                description=f"{control} center stick sensitivity in deg/s",
                default=72.0,
                min=0.0,
                max=1000.0,
            )
        )
        setattr(bpy.types.WindowManager, f"rc_{control.lower()}_max",
            FloatProperty(
                name="Max Rate",
                description=f"{control} maximum rate in deg/s",
                default=800.0,
                min=0.0,
                max=1000.0,
            )
        )
        setattr(bpy.types.WindowManager, f"rc_{control.lower()}_expo",
            FloatProperty(
                name="Expo",
                description=f"{control} exponential factor",
                default=0.5,
                min=0.0,
                max=1.0,
            )
        )

    # Throttle properties
    bpy.types.WindowManager.rc_throttle_limit = EnumProperty(
        items=[
            ('OFF', 'Off', 'No limiting'),
            ('SCALE', 'Scale', 'Scale throttle output'),
            ('CLIP', 'Clip', 'Clip throttle output')
        ],
        name="Limit Type",
        default='OFF'
    )
    bpy.types.WindowManager.rc_throttle_limit_amount = FloatProperty(
        name="Limit Amount",
        description="Throttle limit amount",
        default=1.0,
        min=0.0,
        max=1.0,
    )
    bpy.types.WindowManager.rc_throttle_mid = FloatProperty(
        name="Mid",
        description="Throttle mid-point adjustment",
        default=0.5,
        min=0.0,
        max=1.0,
    )
    bpy.types.WindowManager.rc_throttle_expo = FloatProperty(
        name="Expo",
        description="Throttle exponential factor",
        default=0.0,
        min=0.0,
        max=1.0,
    )

classes = (
    OBJECT_OT_AppendDroneCam,
    XR_OT_DroneCamStartStop,
    DRONECAM_OT_refresh_devices,
    DRONECAM_OT_select_device,
    ui.XR_PT_panel,
    ui.XR_PT_preferences_panel,
)

def register():
    bpy.types.WindowManager.modal_running = bpy.props.BoolProperty(default=False)
    bpy.types.WindowManager.dronecam_show_inputs = bpy.props.BoolProperty(
        name="Show Controller Inputs",
        default=False
    )
    bpy.types.WindowManager.dronecam_show_rates = bpy.props.BoolProperty(
        name="Show Rate Controls",
        default=False
    )
    
    # Change from sensitivity to rate props
    register_rate_props()
    
    for cls in classes:
        try:
            bpy.utils.register_class(cls)
        except ValueError as e:
            # If already registered, unregister and try again
            bpy.utils.unregister_class(cls)
            bpy.utils.register_class(cls)
    
    # Add timer for RC value updates
    if not bpy.app.timers.is_registered(update_rc_values):
        bpy.app.timers.register(update_rc_values)

def unregister():
    if bpy.app.timers.is_registered(update_rc_values):
        bpy.app.timers.unregister(update_rc_values)

    # Clean up all window manager properties
    del bpy.types.WindowManager.modal_running
    del bpy.types.WindowManager.dronecam_show_inputs
    del bpy.types.WindowManager.dronecam_show_rates
    
    # Clean up rate properties
    for control in ["Yaw", "Pitch", "Roll"]:
        delattr(bpy.types.WindowManager, f"rc_{control.lower()}_center")
        delattr(bpy.types.WindowManager, f"rc_{control.lower()}_max")
        delattr(bpy.types.WindowManager, f"rc_{control.lower()}_expo")
    
    # Clean up throttle properties
    delattr(bpy.types.WindowManager, "rc_throttle_limit")
    delattr(bpy.types.WindowManager, "rc_throttle_limit_amount")
    delattr(bpy.types.WindowManager, "rc_throttle_mid")
    delattr(bpy.types.WindowManager, "rc_throttle_expo")

    # Clean up hide_inactive_channels property
    delattr(bpy.types.WindowManager, "hide_inactive_channels")

    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except (ValueError, RuntimeError):
            pass

if __name__ == "__main__":
    register()
