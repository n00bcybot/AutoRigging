import maya.cmds as cmds

jointList = cmds.ls(et="joint")  # create list from selected joints
removeString = "r_"  # define string to remove


def removePrefix(list, prefix):  # recursive function
    for i in list:  #
        if prefix in i:  # as long as this condition is true, the
            list.remove(i)  #
            removePrefix(list, prefix)  # function will keep calling itself


def replaceString(list, string, stringNew):
    for i in list:
        if string in i:
            i.replace(string, stringNew)


removePrefix(jointList, removeString)
x = "_jnt"
y = "_loc"
replaceString(jointList, x, y)