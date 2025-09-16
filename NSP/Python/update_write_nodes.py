# update_write_nodes_v004

import nuke
import os

def update_write_nodes():

    #Create variables
    show = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] 0 end-3")
    seq = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] 1 end-2")
    shot = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] 2 end-1")
    version = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] end end")
    padding = "_%04d"

    writeNodes = nuke.allNodes("Write")

    for node in writeNodes:

        # Check if the node's name contains "Precomp_"
        if "Precomp_" in node.knob("name").value():

            # Find precompName and extension from node
            precompName = node.knob("precomp_name").value()
            extension = node.knob("extension").value()

            procedural_file_path = f"{seq}/{shot}/Nuke/Renders/{precompName}/{version}/{show}_{seq}_{shot}_{precompName}_{version}{padding}.{extension}"

            # Create padding exception for mov
            if extension == "mov":
                procedural_file_path = f"{seq}/{shot}/Nuke/Renders/{precompName}/{version}/{show}_{seq}_{shot}_{precompName}_{version}.{extension}"

            node.knob('name').setValue("Precomp_" + precompName)
            node.knob("file").setValue(procedural_file_path)
            node.knob("proxy").setValue(procedural_file_path)
            node.knob("reload").execute()

            if extension == "exr":

                node.knob('dw_compression_level').setValue(100)
                node.knob('label').setValue("[value compression]")

            else:

                node.knob('label').setValue("")

        # Check if the node's name contains "Final_Out"
        if "Final_Out" in node.knob("name").value():

            # Find extension from node
            extension = node.knob("extension").value()

            procedural_file_path = f"{seq}/{shot}/Nuke/Renders/Main/{version}/{show}_{seq}_{shot}_Main_{version}{padding}.{extension}"

            # Create padding exception for mov
            if extension == "mov":
                procedural_file_path = f"{seq}/{shot}/Nuke/Renders/Main/{version}/{show}_{seq}_{shot}_Main_{version}.{extension}"

            node.knob("file").setValue(procedural_file_path)
            node.knob("proxy").setValue(procedural_file_path)
            node.knob("reload").execute()

            if extension == "exr":

                node.knob('dw_compression_level').setValue(100)
                node.knob('label').setValue("[value compression]")

            else:

                node.knob('label').setValue("")