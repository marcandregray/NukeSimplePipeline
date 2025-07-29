==================INSTALL==================

To install, rename "Dot.nuke" to ".nuke" and merge it with your existing .nuke. You should probably make a backup of your .nuke before doing this.

After installing, launch Nuke and check the Project Settings for documentation. There is also a "README" toolset that you can bring in with the nodegraph tab menu.

All information can be found below as well.


==================README==================

The goal of this pipeline setup is to reduce manual labour and human error while not getting too complicated. It also allows for user and show specific settings. In order for it to work, you must save your script with a specific name and folder structure.

The structure is as follows:

...//Show/Sequence/Shot/Nuke/Scripts/Show_Sequence_Shot_v001.nk

You cannot have '_' or '.' in the file path, but they must be included in the .nk file name as seperators between values.

Values must be the same in the path and .nk file name, for example:

...//AZL/Seq1/0075/Nuke/Scripts/AZL_Seq1_0075_v001.nk

Where:

'...//' is your custom directory up until the show folder
'AZL' is the show name
'Seq1' is the Sequence name
'0075' is the Shot name

Tools in this pipeline work by looking at the location and name of the .nk file, so it is very important that this is right.

Once you save your script correctly, everything else will work.

After saving your script with the correct name and folder structure, your project directory will automatically be set the the "Show" folder. 

This pipeline includes 2 main tools for writing out media that will help you keep things organzied and work faster.

1. "DK_Precomp"

This is a fancy write node that automatically chooses a relative file location to your project directory as well as a name based on your script name, but allows you to choose the exact name of the precomp using a value found in the "Custom Options" tab of the node.

2. "DK_Final_Out"

This uses the same logic as the "DK_Precomp" tool, but will always be called, "Main" and does not let you to choose a different name.

The version of the write node from both of these tools will always match the script version.

Both of these tools will show you the compression method used (.exr only) incase you want to use DWAA compression to save disk space.

You can select any write node and use "Ctrl+R" in order to create a read node with the corresponding media. The new read node will use a relative path from the project directory. Read nodes created this way and any other way will tell you in the label if it was written with DWAA compression.

There is a useful python script called "Relative Paths for Reads" used with "Ctrl+Alt+R" which will force all read nodes in the script to use a relative path, as long as the media referenced lives within the project directory (the show folder).

Because these tools all use relative paths, you should be able to move the entire project folder to any other location and have it work without reads erroring out.

Another useful python tool is, Gizmo to Group ("Alt+L") which turns selected gizmos into a group. You can do "Ctrl+A" then run this tool to turn every gizmo in your script into a group. You might want to do this in order to share your script with another artist who may not have your specific gizmo's installed.

All 3 of these python scripts can be accessed with their hot keys, or by navigating to the top bar and clicking on the "PythonTools" tab.

Inside your .nuke folder, you can open "init.py" and change the variables for "user" and "show" to control user and show specific functionality. To find out what users and shows are available, look inside the "Users" and "Shows" folders. You can add a user or show by creating a subfolder inside one of these locations, and setting the variable in .nuke/init.py to its respective name. The contents of the user or show folder can generally mirror whats inside .nuke, for example you can add a "Toolsets" folder inside a show folder and populate it with some .nk files to have them available while working on that show. Its probably a good idea to have an init.py and menu.py per user and show.
