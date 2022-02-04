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

locatorsList = cmds.ls(sl=True)
string = "_jnt"

thumbLocators = ['locator45', 'locator46', 'locator47']
indexLocators = ['locator28', 'locator29', 'locator30', 'locator31']
middleLocators = ['locator32', 'locator33', 'locator34', 'locator35']
ringLocators = ['locator40', 'locator41', 'locator42', 'locator43']
pinkyLocators = ['locator36', 'locator37', 'locator38', 'locator39']
wristLocators = ['locator26']


allLists = [thumbLocators, indexLocators, middleLocators, ringLocators, pinkyLocators]


for i in allLists:
    spawnJoints(i)
spawnJoints(wristLocators)
for i in allLists:
    cmds.parent(i[0]+string, wristLocators[0]+string)

