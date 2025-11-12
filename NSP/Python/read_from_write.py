# read_from_write_v002

import nuke
import os

def read_from_write():

    selected_nodes = nuke.selectedNodes()
    
    for node in selected_nodes:
        writeNode = node
    
        # Get the relative file path of the write node
        file_path1 = os.path.dirname(nuke.filename(writeNode))
        file_path2 = nuke.tcl("value root.project_directory") + "/"
        if file_path1.startswith(file_path2):
            file_path3 = file_path1.replace(file_path2, '')

        # Create the Read nodes
        sequences = nuke.getFileNameList(file_path1)
        if not sequences:
            nuke.message("Nothing has been written to this location")
            return

        for seq in sequences:
            readNode = nuke.createNode('Read')
            readNode.knob('file').fromUserText(file_path3 + "/" + seq)

            # Get the "exr/compressionName" metadata value
            compression_name = readNode.metadata("exr/compressionName")

            # Set the label of the read node based on the compression name
            if compression_name == ("DWAA"):
                readNode["label"].setValue("[metadata exr/compressionName]")

            else:
                readNode["label"].setValue(None)

        # Move the read node relative to the write node

        readNode.setXpos(writeNode.xpos() + 0)
        readNode.setYpos(writeNode.ypos() + 75)