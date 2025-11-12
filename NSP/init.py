# ----------------------------------
# init.py
# Version: 1.2.1
# Last Updated: 2025/10/08
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
# Set "projects_dir" to a path that exists in your system, ideally where your projects are saved.
# Set "user" and "show" to a folder name that exists inside the "Users" and "Shows" folders respectively inside your .nuke/NSP folder.
# If you don't want to use them, these variables can be set to "None" (don't include quotes around None).
# After setting these variables, save this file and restart Nuke for it to work.
# If there is a settings conflict, user settings will overwrite show settings.
# For example: If you set the default resolution to HD in your user settings, but the show is set to 4K default, nuke will use HD.

##====================================
##=====# Set Projects Directory #=====
##====================================

# Set the "projects_dir" variable to the common path your projects share, like, "Common/Path/To/My/Projects"

projects_dir = None

##====================================
##===========# Set User #=============
##====================================

# Change the "user" variable.

user = None

##====================================
##===========# Set Show #=============
##====================================

# Change the "show" variable.

show = None

##====================================

if user is not None:

	userPath = os.path.join( "Users" , user )
	nuke.pluginAddPath( userPath )

if show is not None:

	showPath = os.path.join( "Shows" , show )
	nuke.pluginAddPath( showPath )
