import maya.cmds as cmds

primaryAxis = cmds.radioButtonGrp(self.radioGroup1, query=True, sl=True)

jointPositions = []
for i in self.fkJoints:
    jointPositions.append(cmds.xform(i, q=1, ws=1, rp=1))

ctrlList = []
for i, j in zip(self.fkJoints, jointPositions):  # Create controllers, rename and position them on the joints

    cmds.xform(cmds.circle(n=i[:-4] + '_ctrl', r=7), t=j)
    ctrlList.append(i[:-4] + '_ctrl')  # Append controllers names to ctrlList

for i in ctrlList:
    if 'Finger' in i or 'thumb' in i:  # If the controller is a finger controller, set smaller radius
        cmds.circle(i, e=True, r=2)

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
for i, j in zip(ctrlList, self.fkJoints):
    offsetList.append(cmds.group(i, name=i[:-4] + 'offset'))  # Group each controller and add the name to a list

for i, j, o in zip(ctrlList, self.fkJoints, offsetList):
    cmds.matchTransform(o, j)
    cmds.makeIdentity(o, apply=True, translate=True)  # Freeze transformations
    cmds.makeIdentity(i, apply=True)  # Freeze transformations
    cmds.delete(i, constructionHistory=True)  # Delete construction history
    cmds.parentConstraint(i, j, maintainOffset=False)  # Constrain joints to controls

for i, j in zip(ctrlList[:-1], offsetList[:-1]):  #
    offset = offsetList[offsetList.index(j) + 1]
    ctrl = ctrlList[ctrlList.index(i)]
    cmds.parent(offset, ctrl)  # Parent controls under each other

for i in offsetList[
         :-1]:  # Parent fingers controls. If 'Nub' is in item (as in, 'i' is the last joint in the hierarchy),
    if 'Nub' in offsetList[offsetList.index(i)]:
        cmds.parent(offsetList[offsetList.index(i) + 1], 'l_hand_ctrl')  # parent next item under l_hand_ctrl
