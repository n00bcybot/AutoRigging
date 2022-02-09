import sys
import os
sys.path.append(os.path.abspath("C:/Users/fresh/PycharmProjects/AutoRigging"))
from locatorsDict import *
import maya.cmds as cmds

class GuiWindow:

    def __init__(self):

        self.window = 'My Window'
        self.title = 'Rigging Tools'
        self.size = (400, 400)
        self.button = 'Make Locators'

        def spawnTempLocators(args):
            for i, j in zip(locatorsDictionary.keys(),
                            locatorsDictionary.values()):  # Create locators from  template dictionary
                cmds.spaceLocator(position=j, name=i)

        def createDict(args):
            x = cmds.ls(type='locator')  # Create dictionary from locators in the scene,  with locators'
            y = [i.replace('Shape', '') for i in x]
            locatorsDict = {}  # names as keys and their positions in space, as values.
            for i in y:  # Joints will be spawned from this dictionary
                position = cmds.pointPosition(i, world=True)
                locatorsDict[i] = position
            print(locatorsDict)
            return locatorsDict

        def spawnJoints(list, dict):  # Create joints from list
            cmds.select(deselect=True)
            dict_keys = dict.keys()  # Creating dict list of keys from the dictionary

            list_B = []  # Converting it to regular list. This step is necessary, since
            for i in dict_keys:  # dict list is not iterable
                list_B.append(i)

            dictNew = {}  # Declaring the new list
            for i in list:  # For each item in list_A, if the item is in list_B
                if i in list_B:  # add it to the dictNew
                    dictNew[i] = dict[i]  # dictNew[item] becomes the key, = , dictOld[i] gets the
                    # corresponding values
            for i, j in dictNew.items():
                cmds.joint(position=j, n=i + "_jnt")
            cmds.select(deselect=True)

        def selectedList():

            selected = cmds.optionMenuGrp(optMenu, query=True, sl=True) - 1
            return allChains[int(selected)]

        def selectJointChain(args):

            ttt=selectedList()
            if ttt[0] != type(ttt):
                for i in ttt:
                    spawnJoints(i, createDict(args=True))
                else:
                    spawnJoints(ttt, createDict(args=True))

        if cmds.window(self.window, query=True, exists=True):
            cmds.deleteUI(self.window, window=True)

        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        cmds.columnLayout(adjustableColumn=True)

        optMenu = cmds.optionMenuGrp('optMenu', label='Option Menu')
        cmds.menuItem(label='Arm')
        cmds.menuItem(label='Leg')
        cmds.menuItem(label='Spine')
        cmds.menuItem(label='Eys')
        cmds.menuItem(label='Jaw')
        cmds.menuItem(label='Hand')
        cmds.menuItem(label='All')


        cmds.separator(height=10)
        cmds.button(self.button, label='Spawn Locators', command=spawnTempLocators)
        cmds.separator(height=10)

        cmds.separator(height=10)
        cmds.button(self.button, label='Create Dictionary', command=createDict)
        cmds.separator(height=10)

        cmds.separator(height=10)
        cmds.button(self.button, label='Spawn Joints', command=selectJointChain)
        cmds.separator(height=10)

        cmds.showWindow()


windowMain = GuiWindow()
