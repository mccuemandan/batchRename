import maya.cmds as cmds


# define naming and parameters
prefix = "prefix_"
suffix = "_suffix"
countStart = 1

count = countStart
selectedObjects = cmds.ls(sl=True)

for i in selectedObjects:
    currentName = i
    newName = prefix + str(count) + suffix

    cmds.rename( currentName, newName )

    count += 1
