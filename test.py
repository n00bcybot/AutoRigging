import maya.cmds as cmds
'''
jointDict = {}
orient = cmds.ls(et='joint')
selection = cmds.ls(sl=True)

for i in orient:
    if i in selection:
        jointDict[i] = cmds.joint(i, q=True, o=True)

xyz = ['X', 'Y', 'Z']
jointList = jointDict.keys()
valuesList = jointDict.values()
for i, j in zip(valuesList, jointList):
    for x in i:
        if round(x) == 180:
            cmds.setAttr(j + ".jointOrient" + xyz[i.index(x)], 0)

'''
jointList = cmds.ls(et='joint')
cmds.select(jointList[0])
