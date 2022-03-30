import maya.cmds as cmds
import maya.OpenMaya as om

def makeLocator(position):
    cmds.move(position.x, position.y, position.z, cmds.spaceLocator())

def getPoleVectorPosition(armPos, elbowPos, wristPos):
    armVec = om.MVector(armPos[0], armPos[1], armPos[2])
    elbowVec = om.MVector(elbowPos[0], elbowPos[1], elbowPos[2])
    wristVec = om.MVector(wristPos[0], wristPos[1], wristPos[2])

    midPoint = (wristVec - armVec) * 0.5 + armVec
    poleVectorPos = (elbowVec - midPoint) + elbowVec

    makeLocator(poleVectorPos)


def setPVctrlPosition(armPos, elbowPos, wristPos):

    armVec = om.MVector(armPos[0], armPos[1], armPos[2])
    elbowVec = om.MVector(elbowPos[0], elbowPos[1], elbowPos[2])
    wristVec = om.MVector(wristPos[0], wristPos[1], wristPos[2])

    midPoint = (wristVec - armVec) * 0.5 + armVec
    poleVectorPos = (elbowVec - midPoint) + elbowVec
    makeLocator(poleVectorPos)

    cmds.move(wristVec.x, wristVec.y, wristVec.z, 'ikHandle1')
    cmds.move(poleVectorPos.x, poleVectorPos.y, poleVectorPos.z, 'pv_ctrl', rpr=True)

arm_ik_pos = cmds.xform('arm_ik', q=True, ws=True, t=True)
elbow_ik_pos = cmds.xform('elbow_ik', q=True, ws=True, t=True)
wrist_ik_pos = cmds.xform('wrist_ik', q=True, ws=True, t=True)

arm_fk_pos = cmds.xform('arm_fk', q=True, ws=True, t=True)
elbow_fk_pos = cmds.xform('elbow_fk', q=True, ws=True, t=True)
wrist_fk_pos = cmds.xform('wrist_fk', q=True, ws=True, t=True)

setPVctrlPosition(arm_fk_pos, elbow_fk_pos, wrist_fk_pos)