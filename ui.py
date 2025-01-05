import bpy
from bpy.types import Panel, AddonPreferences

class XR_PT_preferences_panel(AddonPreferences):
    bl_idname = __package__

    input_method: bpy.props.EnumProperty(
        items=[
            ('XINPUT', 'XInput', 'Use Xbox controller'),
            ('RC', 'RC Input', 'Use RC transmitter')
        ],
        name="Input Method",
        default='XINPUT'
    )

    # Add property to store selected device
    selected_device: bpy.props.StringProperty(
        name="Selected Device",
        description="Currently selected RC device"
    )

    # Add show_mapping property for collapsible section
    show_mapping: bpy.props.BoolProperty(
        name="Show Function Mapping",
        default=False
    )

    # Function mapping properties (one for each function)
    leftthumb_y_mapping: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Left Thumb Y",
        description="Function for Left Thumb Y axis",
        default='Throttle'
    )

    leftthumb_x_mapping: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Left Thumb X",
        description="Function for Left Thumb X axis",
        default='Yaw'
    )

    rightthumb_y_mapping: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Right Thumb Y",
        description="Function for Right Thumb Y axis",
        default='Pitch'
    )

    rightthumb_x_mapping: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Right Thumb X",
        description="Function for Right Thumb X axis",
        default='Roll'
    )

    # Channel mapping properties (update the items)
    throttle_channel: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 3",  # Changed to show channel number
        description="Function for RC channel 3",
        default='Throttle'
    )

    yaw_channel: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 4",
        description="Function for RC channel 4",
        default='Yaw'
    )

    pitch_channel: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 2",
        description="Function for RC channel 2",
        default='Pitch'
    )

    roll_channel: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 1",
        description="Function for RC channel 1",
        default='Roll'
    )

    # Channel 1 (disabled by default)
    channel_1_enable: bpy.props.BoolProperty(
        name="Enable Channel 1",
        description="Enable/disable channel 1",
        default=False
    )
    channel_1_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 1",
        description="Function for RC channel 1",
        default='Roll'
    )

    # Channel 2 - Roll
    channel_2_enable: bpy.props.BoolProperty(
        name="Enable Channel 2",
        description="Enable/disable channel 2",
        default=True
    )
    channel_2_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 2",
        description="Function for RC channel 2",
        default='Roll'
    )

    # Channel 3 - Pitch
    channel_3_enable: bpy.props.BoolProperty(
        name="Enable Channel 3",
        description="Enable/disable channel 3",
        default=True
    )
    channel_3_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 3",
        description="Function for RC channel 3",
        default='Pitch'
    )

    # Channel 4 - Throttle
    channel_4_enable: bpy.props.BoolProperty(
        name="Enable Channel 4",
        description="Enable/disable channel 4",
        default=True
    )
    channel_4_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 4",
        description="Function for RC channel 4",
        default='Throttle'
    )

    # Channel 5 - Yaw
    channel_5_enable: bpy.props.BoolProperty(
        name="Enable Channel 5",
        description="Enable/disable channel 5",
        default=True
    )
    channel_5_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 5",
        description="Function for RC channel 5",
        default='Yaw'
    )

    channel_6_enable: bpy.props.BoolProperty(
        name="Enable Channel 6",
        description="Enable/disable channel 6",
        default=False
    )
    channel_6_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 6",
        description="Function for RC channel 6",
        default='Throttle'
    )

    # ... Continue for channels 7-18
    channel_7_enable: bpy.props.BoolProperty(
        name="Enable Channel 7",
        description="Enable/disable channel 7",
        default=False
    )
    channel_7_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 7",
        description="Function for RC channel 7",
        default='Throttle'
    )

    # ... (continue pattern for channels 8-18)
    channel_18_enable: bpy.props.BoolProperty(
        name="Enable Channel 18",
        description="Enable/disable channel 18",
        default=False
    )
    channel_18_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 18",
        description="Function for RC channel 18",
        default='Throttle'
    )

    # Channel 8
    channel_8_enable: bpy.props.BoolProperty(
        name="Enable Channel 8",
        description="Enable/disable channel 8",
        default=False
    )
    channel_8_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 8",
        description="Function for RC channel 8",
        default='Throttle'
    )

    # Channel 9
    channel_9_enable: bpy.props.BoolProperty(
        name="Enable Channel 9",
        description="Enable/disable channel 9",
        default=False
    )
    channel_9_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 9",
        description="Function for RC channel 9",
        default='Throttle'
    )

    # Channel 10
    channel_10_enable: bpy.props.BoolProperty(
        name="Enable Channel 10",
        description="Enable/disable channel 10",
        default=False
    )
    channel_10_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 10",
        description="Function for RC channel 10",
        default='Throttle'
    )

    # Channel 11
    channel_11_enable: bpy.props.BoolProperty(
        name="Enable Channel 11",
        description="Enable/disable channel 11",
        default=False
    )
    channel_11_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 11",
        description="Function for RC channel 11",
        default='Throttle'
    )

    # Channel 12
    channel_12_enable: bpy.props.BoolProperty(
        name="Enable Channel 12",
        description="Enable/disable channel 12",
        default=False
    )
    channel_12_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 12",
        description="Function for RC channel 12",
        default='Throttle'
    )

    # Channel 13
    channel_13_enable: bpy.props.BoolProperty(
        name="Enable Channel 13",
        description="Enable/disable channel 13",
        default=False
    )
    channel_13_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 13",
        description="Function for RC channel 13",
        default='Throttle'
    )

    # Channel 14
    channel_14_enable: bpy.props.BoolProperty(
        name="Enable Channel 14",
        description="Enable/disable channel 14",
        default=False
    )
    channel_14_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 14",
        description="Function for RC channel 14",
        default='Throttle'
    )

    # Channel 15
    channel_15_enable: bpy.props.BoolProperty(
        name="Enable Channel 15",
        description="Enable/disable channel 15",
        default=False
    )
    channel_15_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 15",
        description="Function for RC channel 15",
        default='Throttle'
    )

    # Channel 16
    channel_16_enable: bpy.props.BoolProperty(
        name="Enable Channel 16",
        description="Enable/disable channel 16",
        default=False
    )
    channel_16_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 16",
        description="Function for RC channel 16",
        default='Throttle'
    )

    # Channel 17
    channel_17_enable: bpy.props.BoolProperty(
        name="Enable Channel 17",
        description="Enable/disable channel 17",
        default=False
    )
    channel_17_function: bpy.props.EnumProperty(
        items=[
            ('Throttle', 'Throttle', ''),
            ('Yaw', 'Yaw', ''),
            ('Pitch', 'Pitch', ''),
            ('Roll', 'Roll', '')
        ],
        name="Channel 17",
        description="Function for RC channel 17",
        default='Throttle'
    )

    # Add preview property
    rc_preview_active: bpy.props.BoolProperty(
        name="Preview RC Input",
        description="Monitor RC input values",
        default=False
    )

    # Add sensitivity properties for each function and input type
    rc_throttle_sensitivity: bpy.props.FloatProperty(
        name="RC Throttle Sensitivity",
        description="Adjust RC throttle response",
        default=1.0,
        min=0.1,
        max=5.0,
        step=0.1
    )
    rc_yaw_sensitivity: bpy.props.FloatProperty(
        name="RC Yaw Sensitivity",
        description="Adjust RC yaw response",
        default=1.0,
        min=0.1,
        max=5.0,
        step=0.1
    )
    rc_pitch_sensitivity: bpy.props.FloatProperty(
        name="RC Pitch Sensitivity",
        description="Adjust RC pitch response",
        default=1.0,
        min=0.1,
        max=5.0,
        step=0.1
    )
    rc_roll_sensitivity: bpy.props.FloatProperty(
        name="RC Roll Sensitivity",
        description="Adjust RC roll response",
        default=1.0,
        min=0.1,
        max=5.0,
        step=0.1
    )

    # XInput sensitivities
    xinput_throttle_sensitivity: bpy.props.FloatProperty(
        name="XInput Throttle Sensitivity",
        description="Adjust XInput throttle response",
        default=1.0,
        min=0.1,
        max=5.0,
        step=0.1
    )
    xinput_yaw_sensitivity: bpy.props.FloatProperty(
        name="XInput Yaw Sensitivity",
        description="Adjust XInput yaw response",
        default=1.0,
        min=0.1,
        max=5.0,
        step=0.1
    )
    xinput_pitch_sensitivity: bpy.props.FloatProperty(
        name="XInput Pitch Sensitivity",
        description="Adjust XInput pitch response",
        default=1.0,
        min=0.1,
        max=5.0,
        step=0.1
    )
    xinput_roll_sensitivity: bpy.props.FloatProperty(
        name="XInput Roll Sensitivity",
        description="Adjust XInput roll response",
        default=1.0,
        min=0.1,
        max=5.0,
        step=0.1
    )

    # Add new property for hiding inactive channels
    hide_inactive_channels: bpy.props.BoolProperty(
        name="Hide Inactive",
        description="Hide disabled RC channels",
        default=True
    )

    def draw(self, context):
        layout = self.layout
        
        # AREA 1: Input Method Selection
        box = layout.box()
        box.label(text="Input Device", icon='PLUGIN')
        box.prop(self, "input_method", expand=True)
        
        # RC-specific settings
        if self.input_method == 'RC':
            # Device Selection
            box = layout.box()
            box.label(text="RC Device Settings")
            
            from . import RC_input
            devices = RC_input.scan_for_rc_devices()
            
            if not devices:
                box.label(text="No RC devices detected", icon='ERROR')
            else:
                for device in devices:
                    row = box.row()
                    is_selected = self.selected_device == device['name']
                    icon = 'RADIOBUT_ON' if is_selected else 'RADIOBUT_OFF'
                    
                    op = row.operator(
                        "dronecam.select_device", 
                        text=device['name'], 
                        icon=icon,
                        depress=is_selected
                    )
                    op.device_name = device['name']
                    op.device_path = device['path'].decode('utf-8') if isinstance(device['path'], bytes) else device['path']
            
            row = box.row()
            row.operator("dronecam.refresh_devices", icon='FILE_REFRESH')

        # AREA 2: Function Mapping (moved outside RC-specific block)
        box = layout.box()
        row = box.row()
        row.prop(
            self, "show_mapping",
            icon='TRIA_DOWN' if self.show_mapping else 'TRIA_RIGHT',
            icon_only=True, emboss=False
        )
        row.label(text="Function Mapping")
        
        if self.show_mapping:
            col = box.column(align=True)
            input_type = "rc" if self.input_method == 'RC' else "xinput"
            
            # Function mapping UI with sensitivity
            for control in [
                ("leftthumb_y", "Left Thumb Y"),
                ("leftthumb_x", "Left Thumb X"),
                ("rightthumb_y", "Right Thumb Y"),
                ("rightthumb_x", "Right Thumb X")
            ]:
                row = box.row()
                # Label and function dropdown
                split = row.split(factor=0.6)
                sub = split.row()
                sub.label(text=control[1])
                sub.prop(self, f"{control[0]}_mapping", text="")
                # Add sensitivity slider
                function = getattr(self, f"{control[0]}_mapping").lower()
                split.prop(self, f"{input_type}_{function}_sensitivity", text="Sens")

        # AREA 3: Channel Mapping (RC-specific)
        if self.input_method == 'RC' and self.selected_device:
            box = layout.box()
            
            # Title row
            row = box.row()
            row.label(text="RC Channel Assignment")
            
            # Controls row
            row = box.row(align=True)
            row.prop(self, "rc_preview_active", text="Preview", icon='PLAY' if not self.rc_preview_active else 'PAUSE')
            row.prop(self, "hide_inactive_channels", text="Hide Inactive")
            
            # Show channels
            for i in range(1, 19):
                # Skip disabled channels if hide_inactive is enabled
                if self.hide_inactive_channels and not getattr(self, f'channel_{i}_enable'):
                    continue
                    
                row = box.row(align=True)
                # Enable/disable checkbox
                row.prop(self, f'channel_{i}_enable', text="")
                
                # Channel number and current value
                split = row.split(factor=0.4)
                split.label(text=f"Channel {i}")  # Channel number
                
                # Get value from RC input
                from . import RC_input
                value = RC_input.get_channel_value(i)
                if value is not None:
                    split.label(text=f"{value:.2f}")
                else:
                    split.label(text="--")  # Show dashes when no value
                
                # Channel function dropdown (disabled when channel is disabled)
                sub = row.row()
                sub.enabled = getattr(self, f'channel_{i}_enable')
                sub.prop(self, f'channel_{i}_function', text="")  # Removed Channel {i} text since we show it separately

class XR_PT_panel(Panel):
    bl_label = "DroneCam"
    bl_idname = "OBJECT_PT_DroneCam_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "DroneCam"

    def draw(self, context):
        layout = self.layout
        wm = context.window_manager
        prefs = context.preferences.addons[__package__].preferences
        
        # Top row with main controls
        col = layout.column()
        row = col.row()
        row.scale_y = 3
        row.operator("object.append_dronecam")
        if bpy.context.window_manager.modal_running == False:
            row.operator("wm.dronecamstartstop")
        else:
            row.operator("wm.dronecamstartstop", text="Right Click or Esc to Stop", icon="ERROR")
        
        # Settings button
        row = layout.row()
        row.operator("preferences.addon_show", text="", icon='PREFERENCES').module = __package__
        row.label(text="DroneCam Settings")
        
        # Add Sensitivity Controls section
        box = layout.box()
        row = box.row(align=True)
        row.prop(wm, "dronecam_show_rates", 
                icon='TRIA_DOWN' if wm.dronecam_show_rates else 'TRIA_RIGHT',
                icon_only=True, emboss=False)
        row.label(text="Rates")
        
        if wm.dronecam_show_rates:
            # YPR Rates (removed label)
            for control in ["Yaw", "Pitch", "Roll"]:
                col = box.column(align=True)
                col.label(text=f"{control}:")
                row = col.row(align=True)
                row.prop(wm, f"rc_{control.lower()}_center", text="Center")
                row.prop(wm, f"rc_{control.lower()}_max", text="Max")
                row.prop(wm, f"rc_{control.lower()}_expo", text="Expo")
            
            # Throttle Rates
            box.label(text="Throttle:")
            col = box.column(align=True)
            col.prop(wm, "rc_throttle_limit", text="Limit")
            if wm.rc_throttle_limit != 'OFF':
                col.prop(wm, "rc_throttle_limit_amount", text="Amount")
            col.prop(wm, "rc_throttle_mid", text="Mid")
            col.prop(wm, "rc_throttle_expo", text="Expo")
        
        # Collapsible Controller Inputs section
        xinput_reader_empty = bpy.data.objects.get("XInput Reader")
        if xinput_reader_empty is not None:
            box = layout.box()
            row = box.row(align=True)
            row.prop(context.window_manager, "dronecam_show_inputs", 
                    icon='TRIA_DOWN' if context.window_manager.dronecam_show_inputs else 'TRIA_RIGHT',
                    icon_only=True, emboss=False)
            row.label(text="Controller Inputs")
            
            if context.window_manager.dronecam_show_inputs:
                controller_inputs = xinput_reader_empty.items()
                for controller_input in controller_inputs:
                    if type(xinput_reader_empty[controller_input[0]]) == float or int or bool:
                        row = box.row()
                        prop_name = controller_input[0]
                        row.prop(xinput_reader_empty, f'["{prop_name}"]') 