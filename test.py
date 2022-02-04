import maya.cmds as cmds


def spawnJoints(list):
    cmds.select(deselect=True)
    locatorsPosition = []
    for i in list:
        locatorsPosition.append(cmds.pointPosition(i, world=True))
    for i, j in zip(locatorsPosition, list):
        cmds.joint(position=i, n=j+string)
    for i in list:
        cmds.delete(i)

locatorsList = ['locator45', 'locator46', 'locator47']
string = "_jnt"

spawnJoints(locatorsList)