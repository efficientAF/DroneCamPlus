# DroneCam Plus

**DroneCam Plus** is a Blender addon that allows you to fly a camera like a drone using an Xbox360 gamepad or an RC remote as input. This project builds upon the functionality of the DroneCam addon, enhancing the user experience with new features and improved controls.

## Key Features
- **Easy Setup**: Plug in the controller and launch Blender.
- **Simple Installation**: Install the zip file as you would with any addon.
- **Recording Capabilities**: Click "Add DroneCam Plus" to start flying and recording inputs.
- **Physics Parameters**: Change physics parameters on the Drone object Geometry Nodes modifier for customized flight behavior.
- **Manual Control**: Manually rotate the camera on the X-axis to control tilt aggressiveness.
- **Input Mapping**: Map the controller inputs to the different controls.
- **Rate Control**: Adjust the sensitivity and responsiveness of the controls for a more tailored experience.

## Compatibility and Goals

### Backward Compatibility
**DroneCam Plus** is designed to maintain backward compatibility with existing Blend files created using the original DroneCam addon. Users should be able to open projects using the Geometry Nodes setup made for the original DroneCam addon without issues.

### Main Goals of DroneCam Plus
The primary objectives of this fork include:

- **Modularization**: Enhancing the structure of the code to allow for easier updates and maintenance using LLM's. This will facilitate the addition of new features in the future without disrupting existing functionality.
- **Added Inputs**: Introducing new input methods, primarily RC Remotes used in the hobby.
- **Rate Controls**: Implementing Rate controls for a more authentic feel, allowing users to fine-tune their experience.
- **Future Enhancements**: Keeping the door open for additional features and improvements based on user feedback and technological advancements.

### Controls
- **Left Joystick Y** -> Throttle  
- **Left Joystick X** -> Yaw  
- **Right Joystick Y** -> Pitch  
- **Right Joystick X** -> Roll

Controls can be mapped differently as needed and the RC controls may be expanded later to include using the additional channels for various things like Start/Stop or other things. 

## How To Use DroneCam Plus

1. Install the zip file as you would with any addon.
2. Start Blender and plug in your controller.
3. Select your input method: XInput or RC Input.
4. Set up the mappings if they are not correct.
5. Click "Start/Stop" to begin flying, left click to pause.
6. Click "Add DroneCam" if there is no DroneCam object in your scene.
7. To stop the recording, right click the Start/Stop button or Esc.
8. Play the timeline from the first frame to see the results.

## UI Overview

### Sidebar
The DroneCam Plus sidebar provides quick access to the main controls and settings for the addon. Here, you can find:

- **Main Controls**: Start or stop the DroneCam functionality with a single click. If the DroneCam is currently running, the button will indicate how to stop it (Right Click or Esc).
- **DroneCam Settings**: Access the preferences for configuring the addon.
- **Rate Settings**: Configure rates using values similar to "Actual" Rates.
- **Controller Inputs**: Shows the inputs from your controller in real-time.

### Preferences
In the Preferences section, you can customize various settings related to input methods and function mappings:

- **Input Method**: Choose between **XInput** (for Xbox controllers) and **RC Input** (for RC transmitters).
- **Device Selection**: If using RC Input, select your currently connected RC device from the available options.
- **Function Mapping**: Assign specific functions to the joystick axes and buttons. You can customize the mappings for:
- Left Thumb Y
- Left Thumb X
- Right Thumb Y
- Right Thumb X
  
- **Channel Mapping**: Configure the functions for each RC channel (up to 18 channels). You can enable or disable channels and assign specific functions to each.
- **Sensitivity Settings**: Adjust the sensitivity for each control type (RC and XInput) to fine-tune the responsiveness of the controls.

This UI structure allows for a streamlined experience, making it easy to set up and customize your DroneCam Plus controls according to your preferences.


## Future Plans and Enhancements

As development continues, there are several features and improvements planned for **DroneCam Plus**:

- **Throttle Rate Implementation**: Full implementation of the Throttle rate aspects, including Scale and Clip settings, to provide users with more control over throttle responsiveness.

- **Non-Flight Triggers**: Implementing a system for non-flight triggers, allowing users to set up custom actions to be performed from the controller, such as Start/Stop, camera angle, "fire", etc.
  
- **Presets for Rates**: Introducing a presets feature within the Rates control, allowing users to save and quickly switch between different sensitivity and responsiveness settings tailored to their preferences.

- **Open to Suggestions**: I welcome feedback and suggestions from users to enhance the functionality and usability of DroneCam Plus. If you have ideas for new features or improvements, please feel free to reach out!


## Troubleshooting

If you encounter issues:
- Delete the DroneCam Collection and all its content.
- Purge Unused Data (File -> Cleanup).
- Click the "Add DroneCam Plus" button, and everything should work again.

## Links
- [DroneCam Plus Repository](https://github.com/efficientAF/DroneCamPlus)

## Original Addon Links
- [DroneCam Repository](https://github.com/globglob3D/DroneCam)
- [Gumroad Page for DroneCam](https://globglob.gumroad.com/l/dronecam-blender-addon)
- [YouTube Channel](https://www.youtube.com/@globglob3D)
- [Twitter](https://x.com/globglob3D)

## Acknowledgments
This project is built upon the foundation laid by the DroneCam addon. Special thanks to [Arthur Blaquart (globglob3D)](https://github.com/globglob3D) for their work and inspiration.
