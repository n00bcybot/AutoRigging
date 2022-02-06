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

def spawnJoints(list):                                                  #
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
    for i, j in locatorsDict.items():
        if i in list:
            cmds.joint(position=j, n=i + "_jnt")
#######################################################################################################################
locatorsList = ['COMOffset_loc', 'COM_loc', 'head01_loc', 'head02_loc', 'headNub_loc', 'jawNub_loc', 'jaw_loc',
                'l_calf_loc', 'l_clavicleNub_loc', 'l_clavicle_loc', 'l_eyeNub_loc', 'l_eye_loc', 'l_foreArm_loc',
                'l_hand_loc', 'l_heel_loc', 'l_indexFinger01_loc', 'l_indexFinger02_loc', 'l_indexFinger03_loc',
                'l_indexFingerNub_loc', 'l_middleFinger01_loc', 'l_middleFinger02_loc', 'l_middleFinger03_loc',
                'l_middleFingerNub_loc', 'l_pinkyFinger01_loc', 'l_pinkyFinger02_loc', 'l_pinkyFinger03_loc',
                'l_pinkyFingerNub_loc', 'l_ringFinger01_loc', 'l_ringFinger02_loc', 'l_ringFinger03_loc',
                'l_ringFingerNub_loc', 'l_thigh_loc', 'l_thumb01_loc', 'l_thumb02_loc', 'l_thumbNub_loc',
                'l_toeNub_loc', 'l_toe_loc', 'l_upperArm_loc', 'neck01_loc', 'neck02_loc', 'pelvis_loc',
                'root_loc', 'spine01_loc', 'spine02_loc', 'spine03_loc', 'spine04_loc']

spawnJoints(locatorsList)

########################################################################################################################

def compareLists(list1, list2):             # Compares a list to another and produces a new list in the same order
    newList = []                            # like the first one out of the second one
    for i in list1:
         if i == list2[list2.index(i)]:
             newList.append(i)
    print(newList)

########################################################################################################################