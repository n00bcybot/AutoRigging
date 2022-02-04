import maya.cmds as cmds

locatorsList = cmds.ls(sl=True)



cmds.select(deselect=True)
locatorsPosition = []
for i in locatorsList:
    locatorsPosition.append(cmds.pointPosition(i, world = True))

for i in locatorsPosition:
    cmds.joint(position = i)


