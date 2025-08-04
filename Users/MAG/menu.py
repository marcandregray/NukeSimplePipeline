# ----------------------------------
# MAG menu.py
# Version: 1.0.0
# Last Updated: 2025/07/24
# ----------------------------------

# --------------------------------------------------------------
#  KNOB DEFAULTS :::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

### Nodes

#VIEWER
nuke.knobDefault('Viewer.overscan', "1000")
nuke.knobDefault('frame_increment', "4")
# nuke.knobDefault('Viewer.hide_input', "1")

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

# --------------------------------------------------------------
#  CUSTOM MENUS : ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

# --- Create Custom Gizmos menu ---
# Remember, it won't appear until there's a menu item...

MyToolsMenu = nuke.menu('Nodes').addMenu('My Tools', icon="DK.png")

#MyToolsMenu.addCommand('ReformatCG', 'nuke.createNode("Reformat_CG_v007.gizmo")')

CustomToolsMenu = nuke.menu('Nodes').addMenu('Custom Tools', icon="ChromAb_Icon_V002.png")

#CustomToolsMenu.addCommand('Point_Projection', 'nuke.createNode("Point_Projection.gizmo")')