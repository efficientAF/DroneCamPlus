import bpy
import hid

# Store channel values globally
channel_values = [0.0] * 18
current_device = None

def open_device(device_path):
    """Open and initialize HID device connection"""
    global current_device
    try:
        if current_device:
            current_device.close()
        
        # Convert path to bytes if it's a string
        if isinstance(device_path, str):
            device_path = device_path.encode('utf-8')
            
        current_device = hid.device()
        current_device.open_path(device_path)
        current_device.set_nonblocking(True)
        print(f"Successfully opened RC device: {device_path}")
        
        # Print device info for debugging
        print(f"Manufacturer: {current_device.get_manufacturer_string()}")
        print(f"Product: {current_device.get_product_string()}")
        return True
    except Exception as e:
        print(f"Failed to open RC device: {e}")
        current_device = None
        return False

def close_device():
    """Close the current HID device"""
    global current_device
    if current_device:
        current_device.close()
        current_device = None
        print("RC device closed")

def update_channel_values():
    """Update channel values from the RC device"""
    global channel_values, current_device
    
    prefs = bpy.context.preferences.addons[__package__].preferences
    
    # Only close device if neither preview nor recording is active
    if not prefs.rc_preview_active and not bpy.context.window_manager.modal_running:
        if current_device:
            close_device()
        return
        
    # Try to open device if not already open
    if not current_device and prefs.selected_device:
        devices = scan_for_rc_devices()
        for device in devices:
            if device['name'] == prefs.selected_device:
                if open_device(device['path']):
                    print("RC device connected and ready for input")
                break
    
    # Read from device
    if current_device:
        try:
            data = current_device.read(64)
            if data:
                # Debug: Show raw data as hex
                hex_data = ' '.join([f'{x:02x}' for x in data])
                # print(f"Received data from RC: {hex_data}")  # Comment out for less spam
                
                # Process all channels
                for i in range(min(18, (len(data) - 1) // 2)):
                    idx = 1 + (i * 2)
                    if idx + 1 < len(data):
                        raw_value = data[idx] | (data[idx + 1] << 8)
                        normalized = (raw_value - 1024) / 1024.0
                        normalized = max(min(normalized, 1.0), -1.0)
                        
                        if getattr(prefs, f"channel_{i+1}_function") == 'Throttle':
                            normalized = (normalized + 1) * 0.5
                        
                        channel_values[i] = normalized
                        
        except Exception as e:
            print(f"Error reading from RC device: {e}")
            close_device()

def get_channel_value(channel_num):
    """Get the current value for a specific channel"""
    if current_device and 1 <= channel_num <= 18:
        return channel_values[channel_num - 1]
    return None  # Return None instead of 0.0 when no device is active

def scan_for_rc_devices():
    """
    Scan for RC transmitters and return a list of recognized device names
    """
    devices = []
    try:
        for device in hid.enumerate():
            # Look for known RC transmitter manufacturers
            manufacturer = device.get('manufacturer_string', '').lower()
            product = device.get('product_string', '').lower()
            
            # Keywords to identify RC transmitters
            rc_keywords = [
                'radiomaster', 
                'edgetx', 
                'tbs', 
                'betaflight',
                'opentx',
                'frsky'
            ]
            
            if any(keyword in manufacturer or keyword in product for keyword in rc_keywords):
                # Store path as string for Blender properties
                path = device['path'].decode('utf-8') if isinstance(device['path'], bytes) else device['path']
                devices.append({
                    'name': f"{device.get('manufacturer_string', 'Unknown')} - {device.get('product_string', 'Device')}",
                    'path': path,
                    'vendor_id': device['vendor_id'],
                    'product_id': device['product_id']
                })
    except Exception as e:
        print(f"Error scanning for RC devices: {e}")
        # For testing, add a dummy device
        devices.append({
            'name': 'TEST: Radiomaster TX16S',
            'path': 'test_path',  # Store as string
            'vendor_id': 0,
            'product_id': 0
        })
    return devices

def get_rc_input_values():
    """Read values from the selected RC device"""
    prefs = bpy.context.preferences.addons[__package__].preferences
    
    # Make sure device is open
    if not current_device and prefs.selected_device:
        devices = scan_for_rc_devices()
        for device in devices:
            if device['name'] == prefs.selected_device:
                if not open_device(device['path']):
                    return {"Throttle": 0.0, "Yaw": 0.0, "Pitch": 0.0, "Roll": 0.0}
                break
    
    # Read latest values
    update_channel_values()
    
    # Map enabled channels to their functions
    result = {"Throttle": 0.0, "Yaw": 0.0, "Pitch": 0.0, "Roll": 0.0}
    
    for i in range(1, 19):
        if getattr(prefs, f'channel_{i}_enable', False):
            function = getattr(prefs, f'channel_{i}_function')
            # Debug print to see what's being mapped
            print(f"Channel {i}: {function} = {channel_values[i-1]}")
            if function in result and channel_values[i-1] is not None:
                result[function] = channel_values[i-1]
    
    # Debug print final values
    print(f"Final RC values: {result}")
    return result 

def apply_rates(input_value, center_sens, max_rate, expo):
    """Apply RC rates to input value"""
    # Apply expo
    expo_value = input_value**3 * expo + input_value * (1 - expo)
    
    # Apply rates
    if abs(input_value) <= 0.5:
        # Center range
        rate = center_sens
    else:
        # Scale up to max rate
        rate = center_sens + (max_rate - center_sens) * ((abs(input_value) - 0.5) * 2)
    
    return expo_value * rate

def apply_throttle_curve(input_value, mid, expo):
    """Apply throttle curve"""
    # Apply mid-point adjustment
    if input_value < mid:
        output = input_value * (mid / 0.5)
    else:
        output = mid + (input_value - mid) * ((1 - mid) / (1 - 0.5))
    
    # Apply expo
    output = output**3 * expo + output * (1 - expo)
    
    return output 