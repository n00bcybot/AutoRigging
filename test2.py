import maya.cmds as cmds

# FK chain for the hand with group controls and constraints

r1 = 1  # radio button, containing the selected axis (x,y,z); based on that, the controls are spawned with normals pointing in the same direction

cmds.select('l_clavicle_jnt', hi=True)
cmds.select('l_upperArm_FK_jnt', hi=True, add=True)
list = cmds.ls(sl=True, et='joint')


jointList = cmds.ls(sl=True, et='joint')
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
        cmds.circle(i, e=True, nr=[1, 0, 0])  # Set normal orientation for the controllers based on primary axis orientation
elif r1 == 2:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 1, 0])
elif r1 == 3:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 0, 1])

offsetList = []
for i, j in zip(ctrlList, jointList):
    offsetList.append(cmds.group(i, name=i[:-4] + 'offset'))  # Group each controller and add the name to a list

for i, j, o in zip(ctrlList, jointList, offsetList):
    cmds.matchTransform(o, j)
    cmds.makeIdentity(o, apply=True, translate=True)  # Freeze transformations
    cmds.makeIdentity(i, apply=True)  # Freeze transformations
    cmds.delete(i, constructionHistory=True)  # Delete construction history
    cmds.parentConstraint(i, j, maintainOffset=True)  # Constrain joints to controls

for i, j in zip(ctrlList[:-1], offsetList[:-1]):  #
    offset = offsetList[offsetList.index(j) + 1]
    ctrl = ctrlList[ctrlList.index(i)]
    cmds.parent(offset, ctrl)  # Parent controls under each other

cmds.parent('l_upperArm_offset', world=True)
cmds.parent('l_thumb01_offset', world=True)
cmds.delete('l_upperArm_offset')
cmds.parent('l_upperArm_FK_offset', 'l_clavicle_ctrl')

for i in offsetList[0:-4]:  # Parent fingers controls. If 'Nub' is in item (as in, 'i' is the last joint in the hierarchy),
    if 'Nub' in offsetList[offsetList.index(i)] or 'l_hand_offset' in offsetList[offsetList.index(i)]:
        cmds.parent(offsetList[0:-4][offsetList.index(i) + 1], 'l_hand_FK_ctrl')  # parent next item under l_hand_ctrl
