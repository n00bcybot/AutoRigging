import maya.cmds as cmds

jointList = cmds.ls(et='joint')

a = []
for i in jointList:
    a.append(cmds.joint(i, q=True, o=True))

for i, j in zip(a, jointList):
    print(j,i)
