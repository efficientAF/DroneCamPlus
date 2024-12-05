# DroneCam

This is a Blender addon to fly a camera like a drone using a Xbox360 gamepad as input. 

It's a fork of XinputReader: https://github.com/Erindale/XinputReader

What I've made is a physic system made in Geometry Nodes to handle the flying of the drone that the camera attach to.
I've also added buttons to the XInputReader original interface for keyframing your inputs as you fly, to be able to replay and render your camera movements.
And a button to append the drone rig.

# How To Use

Install the zip file as you would with any addon
Click Add Drone
Click Monitor Controller
Click Start Recording to record your inputs each frames
Click Stop Recording to stop. This will also cancel the monitoring of inputs.

You do not have to Start Recording to fly the drone. Just press play on the timeline to be able to fly it in the scene.
You can change physics parameters on the Drone object Geometry Nodes modifier.
