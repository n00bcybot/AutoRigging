from locators import *
import maya.cmds as cmds


class GuiWindow:


    def __init__(self):
        self.window = 'My Window'
        self.title = 'Rigging Tools'
        self.size = (400, 400)
        self.button = 'Make Locators'

        def vertexLocator(self):   # the only way I was able to import function from other file was to create a
            removePrefix(jointList, removeString)      # new one with the imported one

        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)

        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        cmds.columnLayout(adjustableColumn=True)

        cmds.separator(height=20)
        cmds.button(self.button, label='Make Locators', command=vertexLocator)
        cmds.separator(height=20)

        cmds.showWindow()




windowMain = GuiWindow()