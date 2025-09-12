import nuke
import os

def replace_with_relPath():
        
    selectedNodes = nuke.selectedNodes("Read")
    projPath = nuke.tcl("value root.project_directory")
    
    for n in selectedNodes:
      path = n.knob('file').value()
      new_path = path.replace(projPath + "/",'')
      n.knob('file').setValue(new_path)
