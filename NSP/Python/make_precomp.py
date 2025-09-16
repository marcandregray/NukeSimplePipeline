# make_precomp_v006

import nuke

def make_precomp():

	#Create variables
	show = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] 0 end-3")
	seq = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] 1 end-2")
	shot = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] 2 end-1")
	version = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] end end")
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
		writeNode.knob('name').setValue("Precomp_" + precompName)
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
