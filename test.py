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
jointDict = {}  # Create dictionary with the names and positions of the selected joints
for i in jointList:
    jointDict[i] = cmds.xform(i, q=1, ws=1, rp=1)

ctrlList = []
for i, j in zip(jointDict.keys(), jointDict.values()):  # Create controllers, rename and position them on the joints

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
    cmds.matchTransform(i, j, rot=True)

ctrlList.reverse()  # Reverse list so each item can be parented to the next one in the list
for i in ctrlList:  #
    index = ctrlList.index(i)
    cmds.parent(ctrlList[index], ctrlList[index + 1])
    if index == len(ctrlList) - 2:  # When the loop gets to the last index, break to avoid index out of range error
        break
cmds.select(deselect=True)
ctrlList.reverse()


for i, j in zip(ctrlList, jointList):
    cmds.setAttr(i + '.offsetParentMatrix', tuple(cmds.getAttr(i + '.xformMatrix')), type='matrix')  # Copy all values from transform attributes to Offset Parent Matrix
    # This way the values can be zeroed and the controller remains clean
    cmds.setAttr(i + '.translate', 0, 0, 0, type='double3')  # Zero out translation and rotation (scale and shear should be already zeroed)
    cmds.setAttr(i + '.rotate', 0, 0, 0, type='double3')
    cmds.select(deselect=True)
    cmds.connectAttr(i + '.worldMatrix[0]', j + '.offsetParentMatrix', force=True)  # Connect controllers world matrix to OPM
    cmds.setAttr(j + '.translate', 0, 0, 0, type='double3')  # Zero out translation and orientation on the joint
    cmds.setAttr(j + '.jointOrient', 0, 0, 0, type='double3')
    if ctrlList.index(i) > 0:  # The second and the following controllers need to account for the values of the parent, so another node to offset them is needed
        mm1 = cmds.shadingNode('multMatrix', asUtility=True, name='multM_'+j[:-4])  # Create multMatrix node and rename it. This node will blend the values and pass them on
        cmds.connectAttr(i + '.worldMatrix[0]', mm1 + '.matrixIn[0]', force=True)  # Connect world matrix[0] of the controller to matrixIn[0] of the blend node
        cmds.connectAttr(jointList[jointList.index(j)-1] + '.parentInverseMatrix', mm1 + '.matrixIn[1]', force=True)  # Connect the root joint's parent inverse matrix
        # to matrixIn[1] to offset parents matrix values, that way taking the hierarchy into account
        cmds.connectAttr(mm1 + '.matrixSum', j + '.offsetParentMatrix', force=True)  # Connect matrixSum from the blend matrix node to next joint OPM