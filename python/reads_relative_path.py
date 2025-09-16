import nuke
import os

# def replace_with_relPath():
        
#     allReads = nuke.allNodes("Read")
#     relPath = os.path.dirname(nuke.script_directory())
    
#     for n in allReads:
#       path = n.knob('file').value()
#       new_path = path.replace(relPath + "/",'')
#       n.knob('file').setValue(new_path)


################################################################################################## Working on Rel path = project dir

def replace_with_relPath():
        
    allReads = nuke.allNodes("Read")
    relPath = os.path.dirname (os.path.dirname (os.path.dirname (os.path.dirname (nuke.script_directory()))))
    
    for n in allReads:
      path = n.knob('file').value()
      new_path = path.replace(relPath + "/",'')
      n.knob('file').setValue(new_path)
