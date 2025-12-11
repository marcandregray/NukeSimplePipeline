# reads_relative_path_v003

import nuke
import os

def replace_with_relPath():

    # Get the node that triggered the callback
    readNode = nuke.thisNode()

    # Define Project Path
    projPath = nuke.tcl("value root.project_directory")

    path = readNode.knob('file').value()
    new_path = path.replace(projPath + "/",'')
    readNode.knob('file').setValue(new_path)        
