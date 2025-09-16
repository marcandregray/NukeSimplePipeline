# make_final_out_v004

import nuke

def make_final_out():

	#Create variables
	show = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] 0 end-3")
	seq = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] 1 end-2")
	shot = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] 2 end-1")
	version = nuke.tcl ("lrange [split [file rootname [file tail [value root.name]]] '_'] end end")
	padding = "_%04d"

	def get_precomp_extension():

		# Display the popup menu
		extension = nuke.getInput("Extension", "exr")
		return extension

	extension = get_precomp_extension()

	# Create padding exception for mov
	if extension == "mov":

		padding = ""

	# Create the procedural file Path and Name
	procedural_file_path = f"{seq}/{shot}/Nuke/Renders/Main/{version}/{show}_{seq}_{shot}_Main_{version}{padding}.{extension}"

	# Check if the user entered a value
	if extension:

		#Create write node
		writeNode = nuke.createNode('NSP_Final_Out.nk')
		writeNode.knob('name').setValue("Final_Out")
		writeNode.knob('file').setValue(procedural_file_path)
		writeNode.knob('proxy').setValue(procedural_file_path)
		writeNode.knob('channels').setValue("rgba")
		writeNode.knob('create_directories').setValue(1)
		writeNode.knob('extension').setValue(extension)

		if extension == "exr":

			writeNode.knob('dw_compression_level').setValue(100)
			writeNode.knob('label').setValue("[value compression]")

	else:
		# User canceled the input, do nothing
		pass
