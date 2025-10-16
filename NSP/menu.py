# ----------------------------------
# menu.py
# Version: 1.1.3
# Last Updated: 2025/10/09
# ----------------------------------

# --------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

import nuke
import platform
import nukescripts
import new_script_generator
import make_precomp
import read_from_write
import update_write_nodes
import reads_relative_path
import gizmoToGroup
import set_read_node_label

# --------------------------------------------------------------
#  KNOB DEFAULTS :::::::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

### Project Settings

# #Set Default Project Directory relative to Script path

#Set Default Project Directory relative to Script path
nuke.knobDefault("Root.project_directory", "[file dir [file dir [file dir [file dir [file dir [value root.name]]]]]]")

#Add documentation to script comment section
nuke.knobDefault("Root.label", "Check out the NSP_README toolset in the node graph for NSP details.")

# -------------------------------------------------------------
#  Custom Behaviours  :::::::::::::::::::::::::::::::::::::::::
# -------------------------------------------------------------

# ============ Read Node Defaults ============

# Show Compression type from metadata if it exists. For checking if an .exr was rendered with DWAA Compression or not
nuke.addOnCreate(set_read_node_label.set_read_node_label, nodeClass="Read")

# Force relative paths if possible.
nuke.addOnCreate(reads_relative_path.replace_with_relPath, nodeClass="Read")

# =========== Update and Refresh Write Nodes on Save ===========

nuke.addOnScriptSave(update_write_nodes.update_write_nodes)

# --------------------------------------------------------------
#  NSP CUSTOM MENU : :::::::::::::::::::::::::::::::::::::::::::
# --------------------------------------------------------------

## Add and populate a menu to the top toolbar called "PythonTools"

# NSP Python Tools
nuke.menu("Nuke").addCommand('PythonTools/Gizmo to Group', 'gizmoToGroup.replaceGizmoWithGroup()', 'alt+l')
nuke.menu("Nuke").addCommand('PythonTools/Read from Write', 'read_from_write.read_from_write()', 'ctrl+r' )

# --- Create Custom Gizmos menu ---
# Remember, it won't appear until there's a menu item...

NSP_ToolsMenu = nuke.menu('Nodes').addMenu('NSP Tools', icon="NSP.png")

# NSP Essentials
NSP_ToolsMenu.addCommand('NSP_New_Script_Generator', 'new_script_generator.new_script_generator()')
NSP_ToolsMenu.addCommand('NSP_Precomp', 'make_precomp.make_precomp()', "ctrl+w", shortcutContext=2)
