import maya.cmds as cmds


def rope(numberOfJoints, spaceBetween, alongAxis, controlRadius):
    index = 0
    jointList = []
    for i in range(numberOfJoints):
        if alongAxis is 'x':
            jointList.append(cmds.joint(name='joint_' + str(i + 1) + '_jnt', position=[index, 0, 0]))
        elif alongAxis is 'y':
            jointList.append(cmds.joint(name='joint_' + str(i + 1) + '_jnt', position=[0, index, 0]))
        elif alongAxis is 'z':
            jointList.append(cmds.joint(name='joint_' + str(i + 1) + '_jnt', position=[0, 0, index]))
        index += spaceBetween
    jointPositions = []
    for i in jointList:
        jointPositions.append(cmds.xform(i, query=True, worldSpace=True, rotatePivot=True))
    ctrlList = []
    for i, j in zip(jointList[:-1], jointPositions[:-1]):  # Create controllers, rename and position them on the joints
        cmds.xform(cmds.circle(name=i[:-4] + '_ctrl', radius=controlRadius), translation=j)
        ctrlList.append(i[:-4] + '_ctrl')
    for i in ctrlList:
        if alongAxis is 'x':
            cmds.circle(i, edit=True, normal=[1, 0, 0])  # Set normal orientation for the controllers based on primary axis orientation
        elif alongAxis is 'y':
            cmds.circle(i, edit=True, normal=[0, 1, 0])
        elif alongAxis is 'z':
            cmds.circle(i, edit=True, normal=[0, 0, 1])
    offsetList = []
    for i, j in zip(ctrlList, jointList):
        offsetList.append(cmds.group(i, name=i[:-4] + 'offset'))  # Group each controller and add the name to a list
        cmds.makeIdentity(apply=True)  # Freeze transformations
        cmds.delete(i, constructionHistory=True)  # Delete construction history
        cmds.parentConstraint(i, j, maintainOffset=True)  # Constrain joints to controls
    for i, j in zip(ctrlList[:-1], offsetList[:-1]):  #
        offset = offsetList[offsetList.index(j) + 1]
        ctrl = ctrlList[ctrlList.index(i)]
        cmds.parent(offset, ctrl)  # Parent controls under each other


rope(10, 10, 'y', 5)
