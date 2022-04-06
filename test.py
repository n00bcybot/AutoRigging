import maya.cmds as cmds
import maya.OpenMaya as om

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

########################################################################################################################

import maya.cmds as cmds

switchCtrlPoints = [(0, 0, 0), (2, 0, -2), (2, 0, -1), (6, 0, -1), (6, 0, -2), (8, 0, 0), (6, 0, 2), (6, 0, 1),
                    (2, 0, 1), (2, 0, 2), (0, 0, 0)]
switchCtrlPCount = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
normal = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

jointList = ['r_upperArm_jnt', 'r_foreArm_jnt', 'r_hand_jnt']

cmds.select('r_upperArm_FK_jnt', hi=True)
fkJoints = cmds.ls(sl=True)

cmds.select('r_upperArm_IK_jnt', hi=True)
ikJoints = cmds.ls(sl=True)


def getPVctrlPosition(armPos, elbowPos, wristPos):
    armVec = om.MVector(armPos[0], armPos[1], armPos[2])  # Create vector for each joint
    elbowVec = om.MVector(elbowPos[0], elbowPos[1], elbowPos[2])
    wristVec = om.MVector(wristPos[0], wristPos[1], wristPos[2])

    midPoint = (wristVec - armVec) * 0.5 + armVec  # Subtract the arm position from the wrist position, multiply by 0.5 to find the midpoint.
    # + armVec places the new vector at the arm's position
    poleVectorPos = (elbowVec - midPoint) * 10 + elbowVec  # Subtract the midpoint from the elbow's and place it on the elbow
    # (+ elbowVec) to find where the pole vector should be. Multiply brackets result to extend position farther out

    cmds.move(poleVectorPos.x, poleVectorPos.y, poleVectorPos.z,
              cmds.curve(n='r_elbow_ctrl', d=True, p=switchCtrlPoints,
                         k=switchCtrlPCount))  # Place locator on the calculated position
    cmds.xform('r_elbow_ctrl', ro=[0, 0, 90])
    changeShapeColor('r_elbow_ctrl', 13)


primaryAxis = 1

ikName = 'r_arm_ikHandle'
ikCtrl = 'r_arm_ikHandle_ctrl'
cmds.ikHandle(name=ikName, startJoint=ikJoints[0], endEffector=ikJoints[2], sol='ikRPsolver')  # Create IK handle
cmds.circle(n=ikCtrl, r=8, nr=normal[primaryAxis - 1])  # Create IK controller and position it on the joint

offsetGroup = cmds.group(name=ikCtrl + '_offset')
cmds.matchTransform(offsetGroup, 'r_hand_jnt')
cmds.parent(ikName, ikCtrl)
cmds.matchTransform(ikCtrl, offsetGroup)
cmds.orientConstraint(ikCtrl, 'r_hand_IK_jnt')
changeShapeColor(ikCtrl, 13)
cmds.makeIdentity(ikName, apply=True)
cmds.makeIdentity(offsetGroup, apply=True, translate=True)  # Freeze transformations
cmds.makeIdentity(ikCtrl, apply=True)
cmds.delete(ikCtrl, constructionHistory=True)

r_IkFkSwitchPosition = cmds.xform(ikJoints[2], q=1, ws=1, rp=1)
r_IkFkSwitchPosition[2] = r_IkFkSwitchPosition[2] - 20
cmds.xform(cmds.curve(n='r_IK_FK_switch', d=True, p=switchCtrlPoints, k=switchCtrlPCount), t=r_IkFkSwitchPosition)
changeShapeColor('r_IK_FK_switch', 18)

cmds.addAttr(longName='r_IK_FK_switch', attributeType='double', min=0, max=1, defaultValue=0)
cmds.setAttr('r_IK_FK_switch' + '.r_IK_FK_switch', edit=True, keyable=True)
cmds.makeIdentity('r_IK_FK_switch', apply=True)
cmds.delete('r_IK_FK_switch', constructionHistory=True)

arm_ik_pos = cmds.xform('r_upperArm_IK_jnt', q=True, ws=True,
                        t=True)  # Query positions in space of the IK joints and feed them
elbow_ik_pos = cmds.xform('r_foreArm_IK_jnt', q=True, ws=True,
                          t=True)  # to the function, so you can convert them in vectors
wrist_ik_pos = cmds.xform('r_hand_IK_jnt', q=True, ws=True, t=True)

getPVctrlPosition(arm_ik_pos, elbow_ik_pos, wrist_ik_pos)

cmds.makeIdentity('r_elbow_ctrl', apply=True)
cmds.delete('r_elbow_ctrl', constructionHistory=True)
cmds.group(name='r_elbow_ctrl' + '_offset')
cmds.matchTransform(cmds.poleVectorConstraint('r_elbow_ctrl', ikName), 'r_hand_IK_jnt')

cmds.shadingNode('reverse', asUtility=True, name='r_IkFkReverse')
cmds.connectAttr('r_IK_FK_switch.r_IK_FK_switch', 'r_IkFkReverse.inputX')
for i, j, f in zip(jointList, ikJoints, fkJoints):
    cmds.connectAttr('r_IK_FK_switch.r_IK_FK_switch', i + '_parentConstraint1.' + j + 'W1', force=True)
    cmds.connectAttr('r_IkFkReverse.outputX', i + '_parentConstraint1.' + f + 'W0', force=True)

cmds.connectAttr('r_IK_FK_switch.r_IK_FK_switch', 'r_arm_ikHandle_ctrl_offset.visibility', force=True)
cmds.connectAttr('r_IK_FK_switch.r_IK_FK_switch', 'r_elbow_ctrl_offset.visibility', force=True)
cmds.connectAttr('r_IkFkReverse.outputX', 'r_upperArm_FK_offset.visibility', force=True)