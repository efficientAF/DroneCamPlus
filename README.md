# DroneCam

This is a Blender addon to fly a camera like a drone using a Xbox360 gamepad as input. 

Why? It's fun, it makes for realistic camera movements, it's fast. Add the drone, click record, fly around the scene, and then render the results.

It relies on a Physic Simulation made in Geometry Nodes to handle the flying of the drone that the camera attach to.

DroneCam is a fork of XinputReader: https://github.com/Erindale/XinputReader which handle all the gamepad inputs. 

# How To Use

Install the zip file as you would with any addon

Click Add Drone

Click Monitor Controller

Click Start Recording to record your inputs each frames

Click Stop Recording to stop. This will also cancel the monitoring of inputs.

You do not have to Start Recording to fly the drone. Just press play on the timeline to be able to fly it in the scene.

You can change physics parameters on the Drone object Geometry Nodes modifier. 

You can manually rotate the camera on the X axis to control the tilt aggressiveness. 

# Controls

Left Joystick Y -> Throttle  
Left Joystick X -> Yaw  
Right Joystick Y -> Pitch  
Right Joystick X -> Roll  

