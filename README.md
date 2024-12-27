# DroneCam

This is a Blender addon to fly a camera like a drone using a Xbox360 gamepad as input. Only work on Windows.

Why? It's fun, it makes for realistic camera movements, it's fast. Add the drone, click record, fly around the scene, and then render the results.

It relies on a Physic Simulation made in Geometry Nodes to handle the flying of the drone that the camera attach to.

DroneCam is a fork of XinputReader: https://github.com/Erindale/XinputReader which handle all the gamepad inputs. 

# How To Use

Plug the controller and launch Blender

Install the zip file as you would with any addon

Click Add DroneCam

Click Start/Stop to start flying and recording inputs. You can click it again to pause.

Right Click Start/Stop to stop the recording

Play the timeline from the first frame to see the results

You can change physics parameters on the Drone object Geometry Nodes modifier.

You can manually rotate the camera on the X axis to control the tilt aggressiveness.

If things go wrong and it's not working anymore:
- Delete the DroneCam Collection and all it's content
- Purge Unused Data (File -> Cleanup)
- Click the Add DroneCam button and everything should work again

# Controls

Left Joystick Y -> Throttle  
Left Joystick X -> Yaw  
Right Joystick Y -> Pitch  
Right Joystick X -> Roll  

# Links

[Gumroad Page for DroneCam](https://globglob.gumroad.com/l/dronecam-blender-addon)
[Youtube channel](https://www.youtube.com/@globglob3D)
[Twitter](https://x.com/globglob3D)

