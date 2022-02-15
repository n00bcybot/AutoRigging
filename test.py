import sys
import os
sys.path.append(os.path.abspath("C:/Users/fresh/PycharmProjects/AutoRigging"))
import maya.cmds as cmds

'''
jointList = cmds.ls(et='joint')

jointPosition = []
for i in jointList:
   jointPosition.append(cmds.xform(i, q=1,ws=1,rp=1))

for i in jointPosition:
   cmds.spaceLocator(position=i)
'''



jointList = cmds.ls(et="joint")
prefix = "r_"

def removePrefix(list):
    for i in list:
        if prefix in i:
            list.remove(i)
            removePrefix(list)

removePrefix(jointList)

jointPosition = []
for i in jointList:
    jointPosition.append(cmds.xform(i, q=1, ws=1, rp=1))

y = []
for i in jointPosition:
    y.append(i)

locatorsList = []
for i, j in zip(jointPosition, jointList):
    locatorsList.append(cmds.spaceLocator(position=i, name=(j.replace("_jnt", "_loc"))))

x = []
for i in locatorsList:
    x.append(i[0])

namesValues = {}
nameValues = dict(zip(x, y))

for key, value in nameValues.items():
    print(key, ' : ', value)

'''


def renameJoint(jointList, newList):
    for i in jointList:
        if '_r' in i:
            cmds.rename(i, newList[int(i[0:])] + '_jnt')



renameJoint(allJoints, removePrefix(allJoints))




def spawnTempLocators():
    for i, j in zip(locatorsDictionary.keys(),
                    locatorsDictionary.values()):       # Create locators from  template dictionary
        cmds.spaceLocator(position=j, name=i)


def createDict():
    x = cmds.ls(type='locator')                         # Create dictionary from locators in the scene,  with locators'
    y = [i.replace('Shape', '') for i in x]
    locatorsDict = {}                                   # names as keys and their positions in space, as values.
    for i in y:                                         # Joints will be spawned from this dictionary
        position = cmds.pointPosition(i, world=True)
        locatorsDict[i] = position
    print(locatorsDict)
    return locatorsDict


def spawnJoints(list, dict):                            # Create joints from list
    cmds.select(deselect=True)
    dict_keys = dict.keys()                             # Creating dict list of keys from the dictionary

    list_B = []                                         # Converting it to regular list. This step is necessary, since
    for i in dict_keys:                                 # dict list is not iterable
        list_B.append(i)

    dictNew = {}                                        # Declaring the new list
    for i in list:                                      # For each item in list_A, if the item is in list_B
        if i in list_B:                                 # add it to the dictNew
            dictNew[i] = dict[i]                        # dictNew[item] becomes the key, = , dictOld[i] gets the
                                                        # corresponding values
    for i, j in dictNew.items():  # Creating the chain by iterating over the keys and the values
        cmds.joint(n=i.replace('_loc', '_jnt'), position=j)
                        # in the dictionary
    cmds.select(deselect=True)

    orientJoints=cmds.ls(type='joint')                  # Orient all joints
    for i in orientJoints:
        cmds.joint(i, e=True, zso=True, oj='xyz')

    x = cmds.ls(type='locator')                         # Delete locators corresponding to the selected list
    y = [i.replace('Shape', '') for i in x]
    for i in y:
        if i in list:
            cmds.delete(i)

spawnTempLocators()

for i in allLists:                                      # Spawn skeleton
    spawnJoints(i, createDict())


y=[]                                                    # Parent all fingers to hand joint
for eachlist in handLoc:
    y.append(eachlist[0].replace('_loc', '_jnt'))
for i in y:
    cmds.connectJoint(i, 'l_hand_jnt', pm=True)

cmds.connectJoint('l_thigh_jnt', 'pelvis_jnt', pm=True) # Parent the rest of the chains
cmds.connectJoint('l_clavicle_jnt', 'spine04_jnt', pm=True)
cmds.connectJoint('jaw_jnt', 'head02_jnt', pm=True)
cmds.connectJoint('l_eye_jnt', 'head02_jnt', pm=True)

'''