import nuke
import os

def update_write_nodes():

    #Create variables
    version = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] end end")

    writeNodes = nuke.allNodes("Write")

    for node in writeNodes:

        # Check if the node's name contains "Precomp_" or "Final_Out"
        if "Precomp_" in node.knob("name").value() or "Final_Out" in node.knob("name").value():

            current_file = node['file'].value()
            ht = os.path.split(current_file)

            current_file_path = ht[0]
            current_file_name = ht[1]

            file_path_parts = current_file_path.split("/")
            file_path_parts[-1] = version
            new_file_path = "/".join(file_path_parts)

            file_name_parts = current_file_name.split("_")
            file_name_parts[-2] = version
            new_file_name = "_".join(file_name_parts)

            node.knob("file").setValue(new_file_path + "/" + new_file_name)
            node.knob("proxy").setValue(new_file_path + "/" + new_file_name)
            node.knob("reload").execute()
