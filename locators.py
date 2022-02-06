from locatorsDict import *
import maya.cmds as cmds


########################################################################################################################
# select vertices and spawn locator at each vertex' position

def vertexToLocator():
    vertexList = cmds.ls(selection=True, flatten=True)                     # create list from selected vertices
    vertexPosition = []                                                    # create empty list to add to
    for i in vertexList:                                                   # get position of all selected vertices
        vertexPosition.append(cmds.pointPosition(i, local=True))           #
    for i in vertexPosition:                                               #
        cmds.spaceLocator(position=i)                                      # spawn locator at the positions in the list


########################################################################################################################

jointList = cmds.ls(et="joint")                                            # create list from selected joints
removeString = "r_"                                                        # define string to remove
                                                                           #
                                                                           #
def removePrefix(list, prefix):                                            # recursive function
    for i in list:                                                         #
        if prefix in i:                                                    # as long as this condition is true, the
            list.remove(i)                                                 #
            removePrefix(list, prefix)                                     # function will keep calling itself

########################################################################################################################

def replaceString(inputlist, string, newString, outputList):               # Replace a string with another for each
    for i in inputlist:                                                    # item in list; empty output list must be
        if string in i:                                                    # defined for this to work
            temp = i.replace(string, newString)                            #
            outputList.append(temp)                                        #
    return outputList                                                      #

list = ["r_apple_jnt", "r_pair_jnt", "r_banana_jnt", "r_orange_jnt", "strawberry", "raspberry", "blueberry"]

z = []
x = "_jnt"
y = "_loc"

print(replaceString(list, x, y, z))

########################################################################################################################
# Creates joint chain from locators list

def spawnJoints2(list):                                                  #
    cmds.select(deselect=True)                                          # In case there is anything selected in the
    locatorsPosition = []                                               # scene, this command deselects it - otherwise
    for i in list:                                                      # messes up the command
        locatorsPosition.append(cmds.pointPosition(i, world=True))      #
    for i, j in zip(locatorsPosition, list):                            #
        cmds.joint(position=i, name=j+"_jnt")                           # This line renames the joint
    for i in list:                                                      # This loop deletes all locators use for
        cmds.delete(i)                                                  # the joint creation

########################################################################################################################

def createJoints(list):
    for i, j in thumbLocs.items():
        if i in list:
            cmds.joint(position=j, n=i + "_jnt")

#######################################################################################################################

def compareLists(list1, list2):             # Compares a list to another and produces a new list in the same order
    newList = []                            # like the first one out of the second one
    for i in list1:
         if i == list2[list2.index(i)]:
             newList.append(i)
    print(newList)

########################################################################################################################

def spawnTempLocators():                                                    # Create locators from  template dictionary
    for i, j in zip(locatorsDictionary.keys(), locatorsDictionary.values()):
        cmds.spaceLocator(position=j, name=i)

########################################################################################################################

def createDict():
    x = cmds.ls(type='locator')                     # Create dictionary from locators in the scene,  with locators'
    y = [i.replace('Shape', '') for i in x]
    locatorsDict = {}                               # names as keys and their positions in space, as values.
    for i in y:                                     # Joints will be spawned from this dictionary
        position = cmds.pointPosition(i, world=True)
        locatorsDict[i] = position
    print(locatorsDict)
    return locatorsDict

########################################################################################################################

def spawnJoints(list, dict):                        # Create joints from list
    cmds.select(deselect=True)
    dict_keys=dict.keys()                           # Creating dict list of keys from the dictionary

    list_B=[]                                       # Converting it to regular list. This step is necessary, since
    for i in dict_keys:                             # dict list is not iterable
        list_B.append(i)

    dictNew={}                                      # Declaring the new list
    for i in list:                                  # For each item in list_A, if the item is in list_B
        if i in list_B:                             # add it to the dictNew
            dictNew[i]=dict[i]                      # dictNew[item] becomes the key, = , dictOld[i] gets the
                                                    # corresponding values
    for i, j in dictNew.items():
        cmds.joint(position=j, n=i+"_jnt")
    cmds.select(deselect=True)

########################################################################################################################