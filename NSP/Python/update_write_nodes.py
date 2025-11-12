# update_write_nodes_v007

import nuke
import os

def update_write_nodes():

    #Get script name
    scriptLocation = nuke.scriptName()

    #Get script directory part list
    dirName = os.path.dirname(scriptLocation)
    scriptDirParts = dirName.split("/")
    scriptDirParts.reverse()

    #Get script name part list
    scriptName = os.path.basename(scriptLocation)
    scriptNameParts = scriptName.split("_")
    scriptNameParts.reverse()

    show = scriptDirParts[4]
    seq = scriptDirParts[3]
    shot = scriptDirParts[2]
    version = scriptNameParts[0].split(".")[0]
    padding = "_%04d"

    writeNodes = nuke.allNodes("Write")

    for node in writeNodes:

        # Check if the node contains the "precomp_name" and "extension" knobs
        if node.knob("precomp_name") and node.knob("extension"):

            # Find precompName and extension from node
            precompName = node.knob("precomp_name").value()
            extension = node.knob("extension").value()

            procedural_file_path = f"{seq}/{shot}/Nuke/Renders/{precompName}/{version}/{show}_{seq}_{shot}_{precompName}_{version}{padding}.{extension}"

            # Create padding exception for mov
            if extension == "mov":
                procedural_file_path = f"{seq}/{shot}/Nuke/Renders/{precompName}/{version}/{show}_{seq}_{shot}_{precompName}_{version}.{extension}"

            node.knob('name').setValue("NSP_Precomp_" + precompName)
            node.knob("file").setValue(procedural_file_path)
            node.knob("proxy").setValue(procedural_file_path)
            node.knob("reload").execute()

            if extension == "exr":

                node.knob('dw_compression_level').setValue(100)
                node.knob('label').setValue("[value compression]")

            else:

                node.knob('label').setValue("")
