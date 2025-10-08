# new_script_generator_v003

import nuke
import os

# Import the projects_dir variable from NSP/init.py
from NSP.init import projects_dir

def new_script_generator():

    nsg = nuke.createNode("NSP_New_Script_Generator.nk")
    nsg.knob("proj").setValue(projects_dir)

def calculate_script_name():

    thisNode = nuke.thisNode()

    proj = thisNode.knob("proj").value()
    show = thisNode.knob("show").value()
    seq = thisNode.knob("seq").value()
    shot = thisNode.knob("shot").value()
    version = thisNode.knob("version").value()    

    scriptName = f"{proj}/{show}/{seq}/{shot}/Nuke/Scripts/{show}_{seq}_{shot}_v{version}.nk"

    thisNode.knob("script_name").setValue(scriptName)

def save_script():

    thisNode = nuke.thisNode()
    script_name = thisNode.knob("script_name").value()
    split_path = os.path.split(script_name)

    save_dir = split_path[0]
    save_name = split_path[1]

    # Check if the save directory exists, and create it if it doesn't
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Construct the full save path
    save_path = os.path.join(save_dir, save_name)

    # Save the Nuke script to the new location
    nuke.scriptSaveAs(save_path)
