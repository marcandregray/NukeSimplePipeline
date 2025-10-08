# ----------------------------------
# MAG menu.py
# Version: 1.0.2
# Last Updated: 2025/10/08
# ----------------------------------

import ConnectDot_Functions
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

#VIEWER
nuke.knobDefault('Viewer.overscan', "1000")
#nuke.knobDefault('frame_increment', "4")
#nuke.knobDefault('Viewer.hide_input', "1")

#TRACKER
nuke.knobDefault("Tracker4.label", "Motion: [value transform]\nRef_Frame [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()
['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')

#SICKY NOTE
nuke.knobDefault('StickyNote.note_font_size', "55")
nuke.knobDefault('StickyNote.tile_color', "0x262626ff")

#ROTOPAINT
nuke.knobDefault("RotoPaint.toolbox", "brush")

#UI Knob Color Defaults
UI_nodeList = ["RotoPaint", "Roto", "Transform", "CornerPin2D"]
UI_color = "0xff0000ff"

for n in UI_nodeList:
	nuke.knobDefault(n + ".gl_color", UI_color)

# -------------------------------------------------------------
#  Custom Behaviours  :::::::::::::::::::::::::::::::::::::::::
# -------------------------------------------------------------

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

# --------------------------------------------------------------
#  CUSTOM MENUS : ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# --- Create Custom Gizmos menu ---
# Remember, it won't appear until there's a menu item...

MyToolsMenu = nuke.menu('Nodes').addMenu('My Tools', icon="DK.png")

#MyToolsMenu.addCommand('ReformatCG', 'nuke.createNode("Reformat_CG_v007.gizmo")')

CustomToolsMenu = nuke.menu('Nodes').addMenu('Custom Tools', icon="ChromAb_Icon_V002.png")

#CustomToolsMenu.addCommand('Point_Projection', 'nuke.createNode("Point_Projection.gizmo")')