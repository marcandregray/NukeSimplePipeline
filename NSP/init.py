# ----------------------------------
# init.py
# Version: 1.2.0
# Last Updated: 2025/09/10
# ------------------------------------------------

import nuke
import os

# ---------DEFINE CUSTOM FOLDER STRUCTURE----------

nuke.pluginAddPath('Python')
nuke.pluginAddPath('Icons')
nuke.pluginAddPath('Gizmos')

##====================================
##============== README ==============
##====================================

# Below there are 3 variables that must be set in order for NSP to work correctly.
# "projects_dir" must be set to a path that exists in your system, ideally where your projects are saved.
# "user" and "show" must be set to a folder name that exists inside the "Users" and "Shows" folders respectively inside your .nuke
# If you don't want to use them, the "user" and "show" variables can be set to "None" (don't include quotes around None).
# After setting these variables, save this file and restart Nuke for it to work.
# If there is a settings conflict, user settings will overwrite show settings.
# For example: If you set the default resolution to HD in your user settings, but the show is set to 4K default, nuke will use HD as default.

##====================================
##====== Set Projects Directory ======
##====================================

# Set the "projects_dir" variable to the common path your projects share, like, "Common/Path/To/My/Projects"

projects_dir = "/example/of/path/to/your/Projects"

##====================================
##============ Change User ===========
##====================================

# Change the "user" variable to one that exists. You can also set it to "None" (don't include quotes around None)

user = "dkoss"

if user is not None:

	userPath = os.path.join( "Users" , user )
	nuke.pluginAddPath( userPath )

##====================================
##============ Change Show ===========
##====================================

# Change the "show" variable to one that exists. You can also set it to "None" (don't include quotes around None)

show = None

if show is not None:

	showPath = os.path.join( "Shows" , show )
	nuke.pluginAddPath( showPath )