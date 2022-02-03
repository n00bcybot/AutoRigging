import maya.cmds as cmds


########################################################################################################################
# select vertices and spawn locator at each vertex' position

def vertexToLocator():
    vertexList = cmds.ls(selection=True, flatten=True)                     # create list from selected vertices
    vertexPosition = []                                                    # create empty list to add to
    for i in vertexList:                                                   # get position of all selected vertices
        vertexPosition.append(cmds.pointPosition(i, local=True))
    for i in vertexPosition:
        cmds.spaceLocator(position=i)                                      # spawn locator at the positions in the list


########################################################################################################################

jointList = cmds.ls(et="joint")                                 # create list from selected joints
removeString = "r_"                                             # define string to remove

def removePrefix(list, prefix):                                 # recursive function
    for i in list:                                              #
        if prefix in i:                                         # as long as this condition is true, the
            list.remove(i)                                      #
            removePrefix(list, prefix)                          # function will keep calling itself

########################################################################################################################