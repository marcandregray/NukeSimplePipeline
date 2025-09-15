================INSTALL================

To install, add the "NSP" folder to your .nuke folder.

You must also include the following line inside your .nuke/init.py file:

nuke.pluginAddPath('NSP')

After installing, launch Nuke and check the Project Settings for documentation. There is also a "NSP_README" toolset that you can bring in with the nodegraph tab menu.

All information can be found below as well.


==================README==================

Welcome to Nuke Simple Pipeline (NSP)!  This package is ideal for compositors who are used to a studio pipeline and are starting a personal or freelance project using a vanilla Nuke. The goal of NSP is to automate common tasks in order to reduce manual labour and human error, without getting complicated.

NSP accomplishes this with:

-Ability to control "Show" and "User" environoment
-Automatic Script creation with procedural paths and names
-Automatic Read and Write naming and creation
-Automatic versioning of writes to always match script version
-Ability to create reads sourced from selected writes
-As many relative paths as possible
-Some handy python scripts


=====Getting Started=====

1.
The first step to making NSP work is to open the .nuke/NSP/init.py file and follow the instructions under "README" After updating and saving this init.py,  restart Nuke then move to step 2.

2.
Time to save a script for your new project. In the node graph, create "NSP_New_Script_Generator" using the tab menu. In the node's properties, choose the Show, Sequence, and Shot name you want this script to be for. It is important that this naming pattern is maintained for other tools to work. The values you enter cannot Include spaces, "_" or "." as these are used to seperate values in the script name. Now click the "Calculate Script Name" button to see your result in the "Script Name" field.

It should look something like:

...//Show/Sequence/Shot/Nuke/Scripts/Show_Sequence_Shot_v001.nk

or

...//AZL/Seq1/0075/Nuke/Scripts/AZL_Seq1_0075_v001.nk

Where:

'...//' is your common projects directory up until the show folder
'AZL' is the show name
'Seq1' is the Sequence name
'0075' is the Shot name

If the name looks correct,  click the "Save Script" button to create the path and save the script inside.

======================================================================

NSP includes 2 main tools for writing out media that will help you keep things organzied and work faster. These both use relative paths based on the project directory, which is always set to be the Show folder.

1.
"NSP_Precomp"

When this tool is created in the nodegraph (ctrl + w), a popup menu will appear asking for the Precomp Name and file extension. The name can contain "_" but not "." or spaces. For the extension, "exr" is default, but you can change it to anything like "png" or "mov". After pressing ok it will create the precomp write node with a relative path to your project directory. On the node, there is a tab titled "NSP" where you can update the Precomp Name and file extension. You must save the script for the node to implement your changes.

It should look something like:

Sequence/Shot/Nuke/Renders/PrecompName/v001/Show_Seq_Shot_v001_%04d.exr

2.
"NSP_Final_Out"

This uses the same logic as the "NSP_Precomp" tool, but will always be called, "Main" and is reserved for your shots final render. You can still change to extension incase you want to write out a video instead of an image sequence for final.

======================================================================

===== Create Read Nodes from Writes =====

After writing out files to disk with these tools, you can select a write node and press (ctrl + r) to create a read nodes sourced from the selected writes. Reads created this way use relative paths.

===== Saving and Versioning Up =====

When you save or version up your script, these two tools will automatically update to match the current script version. With this, v025 of a precomp will always be from v025 of the script!

===== DWAA Compression =====

If you want to use DWAA compression to save disk space, all write nodes created with NSP using the exr extension will always have the compression method labelled. This also applies to all read nodes created pointing to a file using DWAA compression. This is so you will always have a reminder for if a file was created using DWAA since it can be almost impossible to tell just by looking at the image. Usually you will want to switch back to Zip (1 scanline) for your final renders to retain pixel accuracy.

======================================================================

===== Some Useful Python Tools =====

1.
Force Relative Paths

This tool forces selected read nodes to use a relative path. It can be accessed from the top bar under the "PythonTool" menu. To use this correctly, you must copy your media somewhere under your project directory (the Show folder). This could for example be a folder called "Elements" next to the "Scripts" folder inside the "Nuke" folder, or anywhere else you choose so long as it is contained within the project directory.

2.
Gizmos to Group

This tool turns selected gizmos in your script into groups. This can be extremely important if you are going to share your script with another artist who is using a different nuke setup since the gizmos you have installed will only work if they are installed on the other system as well. Groups on the other hand are saved inside the script itself, so can always be opened.

Why not always use groups and never use gizmos? Because saving everything in the script can massively increase the size of the script file and make it much slower to read/save.

======================================================================

===== A Note on "Users" and "Shows" =====

The users and Shows folders inside .nuke/NSP are meant to be used as modular addons. Lets say you are working on a project called AZL and you always want the default resolution in Nuke to be 4096x2480 while you are working on the show. You can set this option in the menu.py file inside the .nuke/NSP/Shows/AZL folder, and then set your Show variable inside the NSP/init.py file to AZL. Nuke will now load the settings you specify from the AZL show folder on startup.

This is the same for the .nuke/NSP/Users folder. If you want to use a custom gizmo, python script, or set custom nuke behaviours, you can do it in your Users folder, which will allow you to have different profiles or "Users" you can pick between.
