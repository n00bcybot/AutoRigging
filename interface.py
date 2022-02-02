import maya.cmds as cmds


class MyWindow:
    def __init__(self):
        self.window = 'My Window'
        self.title = 'Rigging Tools'
        self.size = (400, 400)
        self.button = 'button_makeCube'

        def makeCube():
            cmds.polyCube()

        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)

        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        cmds.columnLayout(adjustableColumn=True)

        cmds.separator(height=20)
        cmds.button(self.button, label='Make Cube', command=makeCube)
        cmds.separator(height=20)

        cmds.showWindow()


windowMain = MyWindow()
