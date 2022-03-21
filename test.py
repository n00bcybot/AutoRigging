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

#  FK/IK Setup Python 2.x

r1 = 1

jointList = cmds.ls(sl=True)  # Get list of selected joints
jointPositions = []
for i in jointList:
    jointPositions.append(cmds.xform(i, q=1, ws=1, rp=1))

ctrlList = []
for i, j in zip(jointList, jointPositions):  # Create controllers, rename and position them on the joints

    cmds.xform(cmds.circle(n=i[:-4] + '_ctrl', r=7), t=j)
    ctrlList.append(i[:-4] + '_ctrl')  # Append controllers names to ctrlList
for i in ctrlList:
    if 'Finger' in i or 'thumb' in i:  # If the controller is a finger controller, set smaller radius
        cmds.circle(i, e=True, r=2)

if r1 == 1:
    for i in ctrlList:
        cmds.circle(i, e=True,
                    nr=[1, 0, 0])  # Set normal orientation for the controllers based on primary axis orientation
elif r1 == 2:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 1, 0])
elif r1 == 3:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 0, 1])

for i, j in zip(ctrlList, jointList):  # Match rotations of the controller to the rotation of the respective joint

    cmds.parent(i, j)                   # Parent each controller to each joint
    cmds.matchTransform(i, j, rot=True)  # Match transformations
    cmds.makeIdentity(apply=True)  # Freeze transformations
    cmds.delete(i, ch=True)  # Delete construction history
    cmds.select(i + 'Shape')  # Select shape node
    cmds.select(j, add=True)    # Add respective joint to the selection. Order of selection is important for this to work
    cmds.parent(s=True, r=True)  # Parent the shape node
    cmds.delete(i)  # Delete the transform node
cmds.ikHandle(startJoint=jointList[0], endEffector=jointList[2])  # Create IK handle
cmds.xform(cmds.circle(n='ik_ctrl', r=10, nr=[1, 0, 0]), t=cmds.xform(jointList[2], q=1, ws=1, rp=1))  # Create IK controller and position it on the joint
cmds.parent('ikHandle1', 'ik_ctrl')  # Parent the handle to the control