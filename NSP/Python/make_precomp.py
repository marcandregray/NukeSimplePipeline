# make_precomp_v008

import nuke
import os

def make_precomp():

	#Get script name
	scriptLocation = nuke.scriptName()

	#Get script directory part list
	dirName = os.path.dirname(scriptLocation)
	scriptDirParts = dirName.split("/")
	scriptDirParts.reverse()

	#Get script name part list
	scriptName = os.path.basename(scriptLocation)
	scriptNameParts = scriptName.split("_")
	scriptNameParts.reverse()

	show = scriptDirParts[4]
	seq = scriptDirParts[3]
	shot = scriptDirParts[2]
	version = scriptNameParts[0].split(".")[0]
	padding = "_%04d"

	def get_precomp_name():

	    # Create the popup menu
	    menu = nuke.Panel("Create Precomp")
	    precompName = menu.addSingleLineInput("Precomp Name", "")
	    extension = menu.addSingleLineInput("Extension", "exr")

	    # Show the popup menu and get the user's input
	    if menu.show():
	        return menu.value("Precomp Name"), menu.value("Extension")
	    else:
	        return None, None

	# Get the precomp name and extension from the user
	precompName, extension = get_precomp_name()

	# Create padding exception for mov
	if extension == "mov":

		padding = ""

	# Check if the user entered a value
	if precompName:
		
		# Create the procedural file Path and Name
		procedural_file_path = f"{seq}/{shot}/Nuke/Renders/{precompName}/{version}/{show}_{seq}_{shot}_{precompName}_{version}{padding}.{extension}"

		#Create write node
		writeNode = nuke.createNode('NSP_Precomp.nk')
		writeNode.knob('name').setValue("NSP_Precomp_" + precompName)
		writeNode.knob('file').setValue(procedural_file_path)
		writeNode.knob('proxy').setValue(procedural_file_path)
		writeNode.knob('channels').setValue("rgba")
		writeNode.knob('create_directories').setValue(1)
		writeNode.knob('precomp_name').setValue(precompName)
		writeNode.knob('extension').setValue(extension)

		if extension == "exr":

			writeNode.knob('dw_compression_level').setValue(100)
			writeNode.knob('label').setValue("[value compression]")

	else:
		# User canceled the input, do nothing
		pass
