import sys
import os

sys.path.append(os.path.abspath("C:/Users/fresh/PycharmProjects/AutoRigging"))
from test import *
import maya.cmds as cmds


class GuiWindow:

    def __init__(self):
        self.window = 'My Window'
        self.title = 'Rigging Tools'
        self.size = (400, 400)
        self.button = 'Make Locators'

        def spawnLocators(args):
            spawnTempLocators()

        def int_createDict(args):
            createDict()

        def int_spawnJoints(args):
            spawnJoints(locatorsDictionary, int_createDict)

        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)


        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        cmds.columnLayout(adjustableColumn=True)

        cmds.separator(height=10)
        cmds.button(self.button, label='Spawn Locators', command=spawnLocators)
        cmds.separator(height=10)
        cmds.button(self.button, label='Spawn Joints', command=int_spawnJoints)
        cmds.separator(height=10)

        cmds.showWindow()


windowMain = GuiWindow()

