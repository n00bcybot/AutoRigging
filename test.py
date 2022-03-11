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


r1 = 1

jointList = cmds.ls(sl=True)  # Get list of selected joints
jointDict = {}              # Create dictionary with the names and positions of the selected joints
for i in jointList:
    jointDict[i] = cmds.xform(i, q=1, ws=1, rp=1)

ctrlList = []
for i, j in zip(jointDict.keys(), jointDict.values()):  # Create controllers, rename and position them on the joints

    cmds.xform(cmds.circle(n=i[:-4] + '_ctrl', r=7), t=j)
    ctrlList.append(i[:-4] + '_ctrl') #  Append controllers names to ctrlList
for i in ctrlList:
    if 'Finger' in i or 'thumb' in i:  # If the controller is a finger controller, set smaller radius
        cmds.circle(i, e=True, r=2)

if r1 == 1:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[1, 0, 0])  # Set normal orientation for the controllers based on primary axis orientation
elif r1 == 2:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 1, 0])
elif r1 == 3:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 0, 1])

for i , j in zip(ctrlList, jointList):  # Match rotations of the controller to the rotation of the respective joint
    cmds.matchTransform(i, j, rot=True)
    cmds.makeIdentity(i, apply=True, t=True)  # Freeze transformations only