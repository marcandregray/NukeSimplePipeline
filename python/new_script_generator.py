import nuke
import os

def calculate_script_name():

    thisNode = nuke.thisNode()

    proj = thisNode.knob("proj").value()
    show = thisNode.knob("show").value()
    seq = thisNode.knob("seq").value()
    shot = thisNode.knob("shot").value()

    scriptName = f"{proj}/{show}/{seq}/{shot}/Nuke/Scripts/{show}_{seq}_{shot}_v001.nk"

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