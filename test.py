import os
import sys

sys.path.append(os.path.abspath("C:/Users/fresh/PycharmProjects/AutoRigging"))
from locators import *
import maya.cmds as cmds




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
    for i, j in dictNew.items():
        cmds.joint(position=j, n=i + "_jnt")
    cmds.select(deselect=True)

spawnTempLocators()
for i in allLists:
    spawnJoints(i, createDict())




