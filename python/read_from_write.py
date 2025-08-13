import nuke
import os

# def read_from_write():

#     selected_nodes = nuke.selectedNodes()
    
#     writeNode = None
#     for node in selected_nodes:
#         if node.Class() == "Write":
#             writeNode = node
#             break
    
#     if not writeNode:
#         #nuke.message("Please select a write node.")
#         return
    
#     # Get the relative file path of the write node
    
#     file_path1 = os.path.dirname(nuke.filename(writeNode))
#     file_path2 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(nuke.filename(writeNode))))) + "/"
#     if file_path1.startswith(file_path2):
#         file_path3 = file_path1.replace(file_path2, '')

#     # Create the Read node
    
#     for seq in nuke.getFileNameList(file_path1):
#         readNode = nuke.createNode('Read')
#         readNode.knob('file').fromUserText(file_path3 + "/" + seq)

#         # Get the "exr/compressionName" metadata value
#         compression_name = readNode.metadata("exr/compressionName")

#         # Set the label of the read node based on the compression name
#         if compression_name == ("DWAA"):
#             readNode["label"].setValue("[metadata exr/compressionName]")

#         else:
#             readNode["label"].setValue(None)

#     # Move the read node relative to the write node

#     readNode.setXpos(writeNode.xpos() + 0)
#     readNode.setYpos(writeNode.ypos() + 75)



################################################################################################## Working on Rel path = project dir

def read_from_write():

    selected_nodes = nuke.selectedNodes()
    
    writeNode = None
    for node in selected_nodes:
        if node.Class() == "Write":
            writeNode = node
            break
    
    if not writeNode:
        #nuke.message("Please select a write node.")
        return
    
    # Get the relative file path of the write node
    
    file_path1 = os.path.dirname(nuke.filename(writeNode))
    file_path2 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(nuke.filename(writeNode)))))))) + "/"
    if file_path1.startswith(file_path2):
        file_path3 = file_path1.replace(file_path2, '')

    # Create the Read node
    
    for seq in nuke.getFileNameList(file_path1):
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