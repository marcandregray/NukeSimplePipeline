# ----------------------------------
# DJK menu.py
# Version: 1.0.2
# Last Updated: 2025/10/05
# ----------------------------------

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

#Set Default Format
#nuke.knobDefault("Root.format", "HD_1080")

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
nuke.knobDefault('frame_increment', "4")
nuke.knobDefault('Viewer.hide_input', "1")

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
#  KEYBOARD SHORTCUTS  :::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# Set to legacy shuffle node

nuke.menu('Nodes').addCommand('Channel/Shuffle', 'nuke.createNode("Shuffle1")', index=0, icon='Shuffle.png')
nuke.menu('Nodes').addCommand('Channel/ShuffleCopy', 'nuke.createNode("ShuffleCopy")', index=1, icon='ShuffleCopy.png')

# --------------------------------------------------------------
#  CUSTOM MENUS : ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# --- Create Custom Gizmos menu ---
# Remember, it won't appear until there's a menu item...

MyToolsMenu = nuke.menu('Nodes').addMenu('My Tools', icon="DK.png")

# My Tools
MyToolsMenu.addCommand('MilkShake', 'nuke.createNode("MilkShake.gizmo")')
MyToolsMenu.addCommand('Orbital_Camera', 'nuke.createNode("Orbital_Camera.nk")')
MyToolsMenu.addCommand('ChannelChooser', 'nuke.createNode("ChannelChooser.gizmo")')
MyToolsMenu.addCommand('ExpoBlur', 'nuke.createNode("ExpoBlur.gizmo")')
MyToolsMenu.addCommand('Crop_Overscan', 'nuke.createNode("Crop_Overscan.gizmo")')
MyToolsMenu.addCommand('EdgeScatter', 'nuke.createNode("EdgeScatter.gizmo")')
MyToolsMenu.addCommand('GradeAOV', 'nuke.createNode("GradeAOV.gizmo")')
MyToolsMenu.addCommand('Combine_CC', 'nuke.createNode("Combine_CC.gizmo")')
MyToolsMenu.addCommand('FractalBlur', 'nuke.createNode("FractalBlur.gizmo")')
MyToolsMenu.addCommand('Blocky', 'nuke.createNode("Blocky")')
MyToolsMenu.addCommand('jkUVEdgeExtend', 'nuke.createNode("jkUVEdgeExtend.gizmo")')
MyToolsMenu.addCommand('X_Distort', 'nuke.createNode("X_Distort.gizmo")')
MyToolsMenu.addCommand('ExpressionWaveGenerator', 'nuke.createNode("ExpressionWaveGenerator.gizmo")')
MyToolsMenu.addCommand('bm_OpticalGlow', 'nuke.createNode("bm_OpticalGlow.gizmo")')
MyToolsMenu.addCommand('bm_OpticalLightwrap', 'nuke.createNode("bm_OpticalLightwrap.gizmo")')
MyToolsMenu.addCommand('aPMatte_v2', 'nuke.createNode("aPMatte_v2.gizmo")')
MyToolsMenu.addCommand('apDespill_v2', 'nuke.createNode("apDespill_v2.gizmo")')
MyToolsMenu.addCommand('ImagePlane3D', 'nuke.createNode("ImagePlane3D.gizmo")')
MyToolsMenu.addCommand('GenerateSTMap', 'nuke.createNode("GenerateSTMap.gizmo")')
MyToolsMenu.addCommand('DasGrain', 'nuke.createNode("DasGrain.gizmo")')
MyToolsMenu.addCommand('DasGrainHelper', 'nuke.createNode("DasGrainHelper.gizmo")')
MyToolsMenu.addCommand('Grain_Advanced', 'nuke.createNode("Grain_Advanced.gizmo")')
MyToolsMenu.addCommand('GuidedBlur', 'nuke.createNode("GuidedBlur.gizmo")')
MyToolsMenu.addCommand('GradMagic', 'nuke.createNode("GradMagic.gizmo")')
MyToolsMenu.addCommand('blink_fog_3d', 'nuke.createNode("blink_fog_3d.gizmo")')
MyToolsMenu.addCommand('CAB_SO', 'nuke.createNode("CAB_SO.gizmo")')
MyToolsMenu.addCommand('NormalsRotate', 'nuke.createNode("NormalsRotate.gizmo")')
MyToolsMenu.addCommand('RemoveAdvanced', 'nuke.createNode("RemoveAdvanced.gizmo")')
MyToolsMenu.addCommand('KeyChew', 'nuke.createNode("KeyChew.gizmo")')
MyToolsMenu.addCommand('VectorFrameBlend', 'nuke.createNode("VectorFrameBlend.gizmo")')