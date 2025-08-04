# ----------------------------------
# init.py
# Version: 1.1.3
# Last Updated: 2025/07/26
# ----------------------------------

# ---------DEFINE CUSTOM FOLDER STRUCTURE----------

nuke.pluginAddPath('gizmos')
nuke.pluginAddPath('gizmos/DK_Gizmos')
nuke.pluginAddPath('python')
nuke.pluginAddPath('icons')
nuke.pluginAddPath('higx/PointRender')
nuke.pluginAddPath('ConnectDot')
nuke.pluginAddPath('fonts')

##====================================
##============ Change User ===========
##====================================

# Change the "user" variable to one that exists. You can also set it to: None

user = "DJK"

if user is not None:

	userPath = os.path.join( "Users" , user )
	nuke.pluginAddPath( userPath )

##====================================
##============ Change Show ===========
##====================================

# Change the "show" variable to one that exists. You can also set it to: None

show = None

if show is not None:

	showPath = os.path.join( "Shows" , show )
	nuke.pluginAddPath( showPath )