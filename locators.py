import maya.cmds as cmds

# select vertices and spawn locator at each vertex' position

vertex_list = cmds.ls(sl=True, fl=True)                    # create list from selected vertices
for i in vertex_list:
    print(i)

vertex_position = []                                       # create empty list to add to

for i in vertex_list:                                      # get position of all selected vertices
    vertex_position.append(cmds.pointPosition(i, l=True))
for i in vertex_position:
    position = cmds.spaceLocator(position=i)               # spawn locator at the positions in the list
