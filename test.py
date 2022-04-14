import maya.cmds as cmds

def changeShapeColor(itemName, color):

    cmds.select(itemName)
    shapeNode = cmds.listRelatives(s=True)[0]
    cmds.setAttr(shapeNode + ".overrideEnabled", 1)  # Change locators' color
    cmds.setAttr(shapeNode + ".overrideColor", color)  # to yellow

def createIKcontrols(self, args):
    primaryAxis = cmds.radioButtonGrp(self.radioGroup1, query=True, sl=True)

    left = 'l_'
    right = 'r_'

    def leg_ikControls(side):

        ikName = side + 'leg_ikHandle'
        ikCtrl = side + 'leg_ikHandle_ctrl'

        startJoint = []
        endJoint = []
        if side is left:
            startJoint = self.l_arm_ikJoints[0]
            endJoint = self.l_arm_ikJoints[2]
        elif side is right:
            startJoint = self.r_arm_ikJoints[0]
            endJoint = self.r_arm_ikJoints[2]

        cmds.ikHandle(name=ikName, startJoint=startJoint, endEffector=endJoint, sol='ikRPsolver')  # Create IK handle
        cmds.circle(n=ikCtrl, r=8, nr=self.normal[primaryAxis - 1])  # Create IK controller and position it on the joint

        offsetGroup = cmds.group(name=ikCtrl + '_offset')
        cmds.matchTransform(offsetGroup, side + 'ankle_jnt')
        cmds.parent(ikName, ikCtrl)
        cmds.matchTransform(ikCtrl, offsetGroup)
        cmds.orientConstraint(ikCtrl, side + 'ankle_IK_jnt')
        changeShapeColor(ikCtrl, 13)
        cmds.makeIdentity(ikName, apply=True)
        cmds.makeIdentity(offsetGroup, apply=True, translate=True)  # Freeze transformations
        cmds.makeIdentity(ikCtrl, apply=True)
        cmds.delete(ikCtrl, constructionHistory=True)

        l_IkFkSwitchPosition = cmds.xform(self.l_arm_ikJoints[2], q=1, ws=1, rp=1)
        l_IkFkSwitchPosition[2] = l_IkFkSwitchPosition[2] - 20
        r_IkFkSwitchPosition = cmds.xform(self.r_arm_ikJoints[2], q=1, ws=1, rp=1)
        r_IkFkSwitchPosition[2] = r_IkFkSwitchPosition[2] - 20

        if side is left:
            cmds.xform(cmds.curve(n=side + 'IK_FK_switch', d=True, p=self.switchCtrlPoints, k=self.switchCtrlPCount),
                       t=l_IkFkSwitchPosition)
            changeShapeColor(side + 'IK_FK_switch', 18)
        if side is right:
            cmds.xform(cmds.curve(n=side + 'IK_FK_switch', d=True, p=self.switchCtrlPoints, k=self.switchCtrlPCount),
                       t=r_IkFkSwitchPosition)
            changeShapeColor(side + 'IK_FK_switch', 18)

        cmds.addAttr(longName=side + 'IK_FK_switch', attributeType='double', min=0, max=1, defaultValue=0)
        cmds.setAttr(side + 'IK_FK_switch' + '.' + side + 'IK_FK_switch', edit=True, keyable=True)
        cmds.makeIdentity(side + 'IK_FK_switch', apply=True)
        cmds.delete(side + 'IK_FK_switch', constructionHistory=True)

        arm_ik_pos = cmds.xform(side + 'upperArm_IK_jnt', q=True, ws=True,
                                t=True)  # Query positions in space of the IK joints and feed them
        elbow_ik_pos = cmds.xform(side + 'foreArm_IK_jnt', q=True, ws=True,
                                  t=True)  # to the function, so you can convert them in vectors
        wrist_ik_pos = cmds.xform(side + 'hand_IK_jnt', q=True, ws=True, t=True)

        self.getPVctrlPosition(arm_ik_pos, elbow_ik_pos, wrist_ik_pos, side)

        cmds.makeIdentity(side + 'elbow_ctrl', apply=True)
        cmds.delete(side + 'elbow_ctrl', constructionHistory=True)
        cmds.group(name=side + 'elbow_ctrl' + '_offset')
        cmds.matchTransform(cmds.poleVectorConstraint(side + 'elbow_ctrl', ikName), side + 'hand_IK_jnt')

        cmds.shadingNode('reverse', asUtility=True, name=side + 'IkFkReverse')
        cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', side + 'IkFkReverse.inputX')

        if side is left:
            for i, j, f in zip(self.l_arm_joints, self.l_arm_ikJoints, self.l_arm_fkJoints):
                cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', i + '_parentConstraint1.' + j + 'W1',
                                 force=True)
                cmds.connectAttr(side + 'IkFkReverse.outputX', i + '_parentConstraint1.' + f + 'W0', force=True)
        elif side is right:
            for i, j, f in zip(self.r_arm_joints, self.r_arm_ikJoints, self.r_arm_fkJoints):
                cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', i + '_parentConstraint1.' + j + 'W1',
                                 force=True)
                cmds.connectAttr(side + 'IkFkReverse.outputX', i + '_parentConstraint1.' + f + 'W0', force=True)

        cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', side + 'arm_ikHandle_ctrl_offset.visibility',
                         force=True)
        cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', side + 'elbow_ctrl_offset.visibility',
                         force=True)
        cmds.connectAttr(side + 'IkFkReverse.outputX', side + 'upperArm_FK_offset.visibility', force=True)

    arm_ikControls(left)
    arm_ikControls(right)