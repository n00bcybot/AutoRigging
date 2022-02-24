import maya.cmds as cmds


jointList = cmds.ls(et='joint')
for i in jointList:
    if i == jointList[-1]:
        print(i)
