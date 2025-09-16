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
import ConnectDot_Functions
import read_from_write
import gizmoToGroup
import reads_relative_path
import animatedSnap3D

# --------------------------------------------------------------
#  Add Tools :::::::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# Animated Snap3D

animatedSnap3D.patch_snap3d() # Optional, only for Nuke 14 and 15.0
animatedSnap3D.install()

# --------------------------------------------------------------
#  KNOB DEFAULTS :::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

### Project Settings

# #Set Default Project Directory relative to Script path
# nuke.knobDefault("Root.project_directory", "[file dir [file dir [value root.name]]]")

################################################################################################## Working on Rel path = project dir

#Set Default Project Directory relative to Script path
nuke.knobDefault("Root.project_directory", "[file dir [file dir [file dir [file dir [file dir [value root.name]]]]]]")

#Set Default Format
nuke.knobDefault("Root.format", "HD_1080")

#Add documentation to script comment section
nuke.knobDefault(

    "Root.label", "The goal of this pipeline setup is to reduce manual labour and human error while not getting too complicated. "
    "In order for it to work, you must save your script with a specific name and folder structure.\n"
    "\n"
    "The structure is as follows:\n"
    "\n"
    "...//Show/Sequence/Shot/Nuke/Scripts/Show_Sequence_Shot_v001.nk\n"
    "\n"
    "You cannot have '_' or '.' in the file path, but they must be included in the .nk file name as seperators between values.\n"
    "\n"
    "Values must be the same in the path and .nk file name, for example:\n"
    "\n"
    "...//AZL/Seq1/0075/Nuke/Scripts/AZL_Seq1_0075_v001.nk\n"
    "\n"
    "Where:\n"
    "\n"
    "'...//' is your custom directory up until the show folder\n"
    "'AZL' is the show name\n"
    "'Seq1' is the Sequence name\n"
    "'0075' is the Shot name\n"
    "\n"
    "Tools in this pipeline work by looking at the location and name of the .nk file, so it is very important that this is right.\n"
    "\n"
    "Once you save your script correctly, everything else will work. Check out the README in the nodegraph menu for tool details!\n"

    )

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

# =========== Refresh Write Nodes on Save ===========

def refresh_write_nodes():

	nodes = nuke.allNodes()
 
	for node in nodes:
		if node.Class() == "Write":
			node.knob("reload").execute()

nuke.addOnScriptSave(refresh_write_nodes)

# --------------------------------------------------------------
#  CUSTOM MENUS : ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

## Add and populate a menu to the top toolbar called "Scripts"

nuke.menu("Nuke").addCommand('PythonTools/Gizmo to Group', 'gizmoToGroup.replaceGizmoWithGroup()', 'alt+l')
nuke.menu("Nuke").addCommand('PythonTools/Read from Write', 'read_from_write.read_from_write()', 'ctrl+r' )
nuke.menu("Nuke").addCommand('PythonTools/Relative Paths for Reads', 'reads_relative_path.replace_with_relPath()', 'ctrl+alt+r' )

# --- Create Custom Gizmos menu ---
# Remember, it won't appear until there's a menu item...

MyToolsMenu = nuke.menu('Nodes').addMenu('My Tools', icon="DK.png")

MyToolsMenu.addCommand('MilkShake', 'nuke.createNode("MilkShake_v008.gizmo")')
MyToolsMenu.addCommand('Orbital_Camera', 'nuke.createNode("Orbital_Camera_v001.nk")')
MyToolsMenu.addCommand('ChannelChooser', 'nuke.createNode("ChannelChooser_v002.gizmo")')
MyToolsMenu.addCommand('ExpoBlur', 'nuke.createNode("ExpoBlur_v002.gizmo")')
MyToolsMenu.addCommand('Crop_Overscan', 'nuke.createNode("Crop_Overscan_v005.gizmo")')
MyToolsMenu.addCommand('DK_Precomp', 'nuke.createNode("DK_Precomp_v007.nk")', "ctrl+w", shortcutContext=2)
MyToolsMenu.addCommand('DK_Final_Out', 'nuke.createNode("DK_Final_Out_v006.nk")')
MyToolsMenu.addCommand('EdgeScatter', 'nuke.createNode("EdgeScatter_v004.gizmo")')
MyToolsMenu.addCommand('GradeAOV', 'nuke.createNode("GradeAOV_v004.gizmo")')
MyToolsMenu.addCommand('Combine_CC', 'nuke.createNode("Combine_CC_v002.gizmo")')
MyToolsMenu.addCommand('FractalBlur', 'nuke.createNode("FractalBlur_v006.gizmo")')

CustomToolsMenu = nuke.menu('Nodes').addMenu('Custom Tools', icon="ChromAb_Icon_V002.png")

CustomToolsMenu.addCommand('Blocky', 'nuke.createNode("Blocky")')
CustomToolsMenu.addCommand('jkUVEdgeExtend', 'nuke.createNode("jkUVEdgeExtend.gizmo")')
CustomToolsMenu.addCommand('X_Distort', 'nuke.createNode("X_Distort.gizmo")')
CustomToolsMenu.addCommand('ExpressionWaveGenerator', 'nuke.createNode("ExpressionWaveGenerator.gizmo")')
CustomToolsMenu.addCommand('Point_Projection', 'nuke.createNode("Point_Projection.gizmo")')
CustomToolsMenu.addCommand('bm_OpticalGlow', 'nuke.createNode("bm_OpticalGlow.gizmo")')
CustomToolsMenu.addCommand('bm_OpticalLightwrap', 'nuke.createNode("bm_OpticalLightwrap.gizmo")')
CustomToolsMenu.addCommand('aPMatte_v2', 'nuke.createNode("aPMatte_v2.gizmo")')
CustomToolsMenu.addCommand('apDespill_v2', 'nuke.createNode("apDespill_v2.gizmo")')
CustomToolsMenu.addCommand('ImagePlane3D', 'nuke.createNode("ImagePlane3D.gizmo")')
CustomToolsMenu.addCommand('GenerateSTMap', 'nuke.createNode("GenerateSTMap.gizmo")')
CustomToolsMenu.addCommand('DasGrain', 'nuke.createNode("DasGrain.gizmo")')
CustomToolsMenu.addCommand('DasGrainHelper', 'nuke.createNode("DasGrainHelper.gizmo")')
CustomToolsMenu.addCommand('Grain_Advanced', 'nuke.createNode("Grain_Advanced.gizmo")')
CustomToolsMenu.addCommand('GuidedBlur', 'nuke.createNode("GuidedBlur.gizmo")')
CustomToolsMenu.addCommand('GradMagic', 'nuke.createNode("GradMagic.gizmo")')
CustomToolsMenu.addCommand('blink_fog_3d', 'nuke.createNode("blink_fog_3d.gizmo")')
CustomToolsMenu.addCommand('CAB_SO', 'nuke.createNode("CAB_SO.gizmo")')
CustomToolsMenu.addCommand('NormalsRotate', 'nuke.createNode("NormalsRotate.gizmo")')
CustomToolsMenu.addCommand('RemoveAdvanced', 'nuke.createNode("RemoveAdvanced.gizmo")')
CustomToolsMenu.addCommand('KeyChew', 'nuke.createNode("KeyChew.gizmo")')
CustomToolsMenu.addCommand('VectorFrameBlend', 'nuke.createNode("VectorFrameBlend.gizmo")')