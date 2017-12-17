import pipelineMenu
print "userSetup"

import maya
maya.cmds.scriptJob(event = ["NewSceneOpened", pipelineMenu.loadMenu]) 


