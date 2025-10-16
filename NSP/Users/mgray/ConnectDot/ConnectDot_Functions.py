import nuke 

def createConDot():
    n = nuke.createNode('connectDot')
    n['Refresh'].execute()

def createConDotInput():
    nodeNumber = len(nuke.selectedNodes())
    unHideButton = nuke.PyScript_Knob("UnHideOutputs", "UnHideOutputs", """
hiddenNodes = nuke.thisNode().dependent(nuke.HIDDEN_INPUTS)
for z in hiddenNodes:
    z["hide_input"].setValue(False)
    """)
    HideButton = nuke.PyScript_Knob("HideOutputs", "HideOutputs", """
hiddenNodes = nuke.thisNode().dependent(nuke.INPUTS)
for z in hiddenNodes:
    z["hide_input"].setValue(True)
    """)

    if nodeNumber == 1:
        dotName = nuke.getInput('set dot name', '_out')
        if nuke.exists(dotName):
            nuke.message('This node name already exists!')
            pass
        else:
            Dot = nuke.createNode('Dot', "name " + dotName, inpanel = False)
            Dot['label'].setValue('[value name]')
            Dot['note_font_size'].setValue(int(42))
            Dot.setYpos(Dot.ypos()+ int(100))
            Dot.addKnob(unHideButton)
            Dot.addKnob(HideButton)
    else:
        pass            

condotbar = nuke.toolbar("ConnectDotFunctions")
condotbar.addCommand("Connect Dot", 'ConnectDot_Functions.createConDot()' , ",", shortcutContext=2)
condotbar.addCommand("ConDotInput", 'ConnectDot_Functions.createConDotInput()' , "ctrl+,", shortcutContext=2)

#Install instructions
#-place the ConnectDot folder into your .nuke folder
#-add this line to the init.py - "nuke.pluginAddPath('ConnectDot')"
#-add this line to the menu.py - "import ConnectDot_Functions"
