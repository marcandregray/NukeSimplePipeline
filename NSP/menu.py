# ----------------------------------
# menu.py
# Version: 1.1.2
# Last Updated: 2025/07/26
# ----------------------------------

# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke
import platform
import nukescripts
import new_script_generator
import make_precomp
import make_final_out
import read_from_write
import update_write_nodes
import reads_relative_path
import gizmoToGroup

# --------------------------------------------------------------
#  KNOB DEFAULTS :::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

### Project Settings

# #Set Default Project Directory relative to Script path

#Set Default Project Directory relative to Script path
nuke.knobDefault("Root.project_directory", "[file dir [file dir [file dir [file dir [file dir [value root.name]]]]]]")

#Set Default Format
nuke.knobDefault("Root.format", "HD_1080")

#Add documentation to script comment section
nuke.knobDefault("Root.label", "Check out the README toolset in the node graph for NSP detailed.")

### Nodes

# ----- MOTION BLUR SHUTTER CENTERED ---------------------------

nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur.shutterTime', "0.5")
nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('ScanlineRender.shutteroffset', "centered")
nuke.knobDefault('Card3D.shutteroffset', "centered")

#ROTO
nuke.knobDefault('Roto.cliptype', "0")

#BLUR
nuke.knobDefault('Blur.crop', "0")

#SHUFFLE
nuke.knobDefault('Shuffle1.label', "[value in]")
nuke.knobDefault('Shuffle2.label', "[value in1]")

#STMap
nuke.knobDefault('STMap.uv', "rgb")

#LAYERCONTACTSHEET
nuke.knobDefault('LayerContactSheet.showLayerNames', "true")

#FRAMEHOLD
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')

# -------------------------------------------------------------
#  Custom Behaviours  :::::::::::::::::::::::::::::::::::::::::
# -------------------------------------------------------------

# =========== Read Node Shows Compression name from metadata if it exists =========== 
# Used to check if an .exr was rendered with DWAA Compression or not

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

# Register the function to be called when a read node is created
nuke.addOnCreate(set_read_node_label, nodeClass="Read")

# =========== 3d transform when 3d nodes selected ===========
# Thank you Sami Oms!

def transformThis() :
    try:
        if 'render_mode' in nuke.selectedNode().knobs():
            return nuke.createNode ( 'TransformGeo' )
        else:
            raise ValueError
    except:
        return nuke.createNode ( 'Transform' )

nuke.menu('Nodes').addCommand( 'Transform/Transform', 'transformThis( )', 't')

def mergeThis() :
    try:
        if 'render_mode' in nuke.selectedNode().knobs():
            return nuke.createNode ( 'MergeGeo' )
        else:
            raise ValueError
    except:
        return nuke.createNode ( 'Merge2' )

# =========== Update and Refresh Write Nodes on Save ===========

nuke.addOnScriptSave(update_write_nodes.update_write_nodes)

# --------------------------------------------------------------
#  CUSTOM MENUS : ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

## Add and populate a menu to the top toolbar called "PythonTools"

nuke.menu("Nuke").addCommand('PythonTools/Gizmo to Group', 'gizmoToGroup.replaceGizmoWithGroup()', 'alt+l')
nuke.menu("Nuke").addCommand('PythonTools/Read from Write', 'read_from_write.read_from_write()', 'ctrl+r' )
nuke.menu("Nuke").addCommand('PythonTools/Relative Selected Reads', 'reads_relative_path.replace_with_relPath()', 'ctrl+alt+r' )

# --- Create Custom Gizmos menu ---
# Remember, it won't appear until there's a menu item...

NSP_ToolsMenu = nuke.menu('Nodes').addMenu('NSP Tools', icon="NSP.png")

# NSP Essentials
NSP_ToolsMenu.addCommand('NSP_New_Script_Generator', 'new_script_generator.new_script_generator()')
NSP_ToolsMenu.addCommand('NSP_Precomp', 'make_precomp.make_precomp()', "ctrl+w", shortcutContext=2)
NSP_ToolsMenu.addCommand('NSP_Final_Out', 'make_final_out.make_final_out()')
