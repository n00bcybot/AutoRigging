import maya.cmds as cmds

thumbLocators = ['r_thumb01_loc', 'r_thumb02_loc', 'r_thumbNub_loc']
indexLocators = ['r_indexFinger01_loc', 'r_indexFinger02_loc', 'r_indexFinger03_loc', 'r_indexFingerNub_loc']
middleLocators = ['r_middleFinger01_loc', 'r_middleFinger02_loc', 'r_middleFinger03_loc', 'r_middleFingerNub_loc']
ringLocators = ['r_ringFinger01_loc', 'r_ringFinger02_loc', 'r_ringFinger03_loc', 'r_ringFingerNub_loc']
pinkyLocators = ['r_pinkyFinger01_loc', 'r_pinkyFinger02_loc', 'r_pinkyFinger03_loc', 'r_pinkyFingerNub_loc']

fingerLocators = [thumbLocators, indexLocators, middleLocators, ringLocators, pinkyLocators]

jointList = ['r_upperArm_jnt', 'r_foreArm_jnt', 'r_hand_jnt']

cmds.select('r_upperArm_FK_jnt', hi=True)
fkJoints = cmds.ls(sl=True)

cmds.select('r_upperArm_IK_jnt', hi=True)
ikJoints = cmds.ls(sl=True)

for i, j, o in zip(fkJoints, ikJoints, jointList):
    cmds.parentConstraint(i, j, o, mo=False, w=1)

cmds.select(deselect=True)

primaryAxis = 1

cmds.select('r_clavicle_jnt', hi=True)
cmds.select('r_upperArm_FK_jnt', hi=True, add=True)

jointList = cmds.ls(sl=True, et='joint')

for i in jointList:
    if 'Nub' in i:
        jointList.pop(jointList.index(i))

jointPositions = []
for i in jointList:
    jointPositions.append(cmds.xform(i, q=1, ws=1, rp=1))

ctrlList = []
for i, j in zip(jointList, jointPositions):  # Create controllers, rename and position them on the joints
    cmds.xform(cmds.circle(n=i[:-4] + '_ctrl', r=7), t=j)
    ctrlList.append(i[:-4] + '_ctrl')  # Append controllers names to ctrlList

for i in ctrlList:
    if 'Finger' in i or 'thumb' in i:  # If the controller is a finger controller, set smaller radius
        cmds.circle(i, e=True, r=1.5)

if primaryAxis == 1:
    for i in ctrlList:
        cmds.circle(i, e=True,
                    nr=[1, 0, 0])  # Set normal orientation for the controllers based on primary axis orientation
        changeShapeColor(i, 17)
elif primaryAxis == 2:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 1, 0])
        changeShapeColor(i, 17)
elif primaryAxis == 3:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 0, 1])
        changeShapeColor(i, 17)

offsetList = []
for i, j in zip(ctrlList, jointList):
    offsetList.append(cmds.group(i, name=i[:-4] + 'offset'))  # Group each controller and add the name to a list

for i, j, o in zip(ctrlList, jointList, offsetList):
    cmds.matchTransform(o, j)
    cmds.makeIdentity(o, apply=True, translate=True)  # Freeze transformations
    cmds.makeIdentity(i, apply=True)  # Freeze transformations
    cmds.delete(i, constructionHistory=True)  # Delete construction history
    cmds.parentConstraint(i, j, maintainOffset=False)  # Constrain joints to controls

for i, j in zip(ctrlList[:-1], offsetList[:-1]):  #
    offset = offsetList[offsetList.index(j) + 1]
    ctrl = ctrlList[ctrlList.index(i)]
    cmds.parent(offset, ctrl)  # Parent controls under each other

cmds.parent('r_upperArm_offset', world=True)  # unparent controls for the main joint chain
cmds.parent('r_thumb01_offset', world=True)
cmds.delete('r_upperArm_offset')  # Delete main joint chain controls
cmds.parent('r_upperArm_FK_offset', 'r_clavicle_ctrl')  # Parent FK controls to l_clavicle_ctrl

cmds.select(deselect=True)
fingersGroup = 'r_fingers_ctrl_offset'
fingersCtrl = 'r_fingers_ctrl'

cmds.group(name=fingersGroup, em=True)
cmds.matchTransform(fingersGroup, 'r_hand_jnt')
cmds.makeIdentity(fingersGroup, apply=True, translate=True)  # Freeze transformations
cmds.select(deselect=True)

fingers = []
for i in fingerLocators:
    fingers.append(i[0].replace('loc', 'offset'))

for i in fingers:
    cmds.parent(i, fingersGroup)  # Parent fingers to new group

cmds.parentConstraint('r_hand_jnt', 'r_fingers_ctrl_offset', mo=False, w=1)