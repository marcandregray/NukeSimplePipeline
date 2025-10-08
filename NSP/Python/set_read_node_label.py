# set_read_node_label_v001

import nuke

def set_read_node_label():

    # Get the node that triggered the callback
    readNode = nuke.thisNode()

    # Check if the selected node is a read node
    if readNode.Class() == "Read":

        # Get the "exr/compressionName" metadata value
        compression_name = readNode.metadata("exr/compressionName")

        # Set the label of the read node based on the compression name
        if compression_name == ("DWAA"):
            readNode["label"].setValue("[metadata exr/compressionName]")

        else:
            readNode["label"].setValue(None)
