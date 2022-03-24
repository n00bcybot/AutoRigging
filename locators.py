import maya.cmds as cmds

unreal_mannequin = {

    'head_loc': [8.2638619126872e-06, 165.51602844828014, -3.977627446646858],
    'l_ball_loc': [17.908687880693478, 2.81181185206154, 8.355310421255368],
    'l_calf_loc': [14.217846378676114, 53.06720387760954, -1.8017859321629537],
    'l_calf_twist_01_loc': [15.67396115850173, 32.893706135607246, -4.996794382039765],
    'l_clavicle_loc': [3.7819897413730077, 152.20121691882997, -2.76039310313689],
    'l_foot_loc': [17.076255020957934, 13.465861257241933, -8.073708919254752],
    'l_hand_loc': [56.646010583642266, 111.67965593245782, -0.3351998041427464],
    'l_index_01_loc': [63.04231809825865, 103.81496760732152, 6.766396160326046],
    'l_index_02_loc': [64.67208291637336, 100.07842201856768, 8.094828611568298],
    'l_index_03_loc': [65.43614662886317, 96.83984280692133, 8.762379029579346],
    'l_lowerarm_loc': [37.26461055165504, 126.44545694310006, -11.910640034409289],
    'l_lowerarm_twist_01_loc': [47.32348572350442, 118.78206065542034, -5.903029226847858],
    'l_middle_01_loc': [64.49004584622266, 103.48136006623012, 4.47948690738144],
    'l_middle_02_loc': [66.53083737888583, 99.5042882705984, 5.72493558835176],
    'l_middle_03_loc': [67.43497084518069, 96.06500328430712, 6.542199647001603],
    'l_pinky_01_loc': [64.0250171479494, 103.01749970642601, -0.15891753186560642],
    'l_pinky_02_loc': [65.93712783436042, 100.01513105522378, 0.12659777121641608],
    'l_pinky_03_loc': [67.01243293424089, 97.2392132645236, 0.3546116758554053],
    'l_ring_01_loc': [64.57561403161198, 103.03925411237485, 2.0826432070241383],
    'l_ring_02_loc': [66.59226511813993, 99.19706279536922, 2.9754782457311206],
    'l_ring_03_loc': [67.43409716471196, 95.87318785861014, 3.5501833944477923],
    'l_thigh_loc': [9.00580960969277, 95.29984073270494, -0.5300275251856618],
    'l_thigh_twist_01_loc': [11.710777262279448, 73.38174582095169, -1.1900507569663903],
    'l_thumb_01_loc': [57.477990686854724, 107.63908893459805, 3.876650039211759],
    'l_thumb_02_loc': [57.607466293869095, 105.46737472247214, 7.076845885543532],
    'l_thumb_03_loc': [57.78417013522182, 102.26216620289371, 9.56615323145238],
    'l_upperarm_loc': [17.700220541891962, 149.53024764716957, -9.71100173315968],
    'l_upperarm_twist_01_loc': [18.02264037407829, 149.14981184811705, -9.747251624362109],
    'neck_01_loc': [7.1703705099944316e-06, 156.42101659898393, -5.874689340166416],
    'pelvis_loc': [1.3536841578012896e-28, 96.75060272216797, -1.0561532974243164],
    'root_loc': [0.0, 0.0, 0.0],
    'spine_01_loc': [1.2988677644386279e-06, 107.55629733472321, -0.1652469392414555],
    'spine_02_loc': [3.547265996651281e-06, 126.76314604454366, -1.51601391020198],
    'spine_03_loc': [5.141275897605e-06, 140.029842391107, -3.497939646387775]
}

locTemp = {
    'COMOffset_loc': [0.0, 105.0, 0.0],
    'COM_loc': [0.0, 105, 0.0],
    'head01_loc': [-2.6069044344454757e-07, 162.29514066931262, -3.573263976481437],
    'head02_loc': [-3.94965337055097e-07, 171.14852788195952, -4.589226443506643],
    'headNub_loc': [-1.7498294615581403e-15, 178.64732454094343, -7.2398515053674455],
    'jawNub_loc': [-7.814865691567292e-13, 161.375737440792, 8.559080733573634],
    'jaw_loc': [-7.677378623110254e-13, 164.0049086101554, 1.5995099911410542],
    'l_calf_loc': [9.016487172208775, 55.99999943954483, 4.0000000438007675],
    'l_clavicleNub_loc': [13.000593365381423, 148.65536599425872, -0.46805474032901184],
    'l_clavicle_loc': [0.5, 148.14189486770232, 4.467180828980827],
    'l_eyeNub_loc': [2.8762510108536112, 169.08230670451212, 8.743195847205346],
    'l_eye_loc': [2.8762517261093254, 169.08230670451212, 7.192147091559658],
    'l_foreArm_loc': [38.47961368255215, 148.65537316436195, -1.872071462890321],
    'l_hand_loc': [63.92736759544309, 148.6553737316454, -0.15012761776273598],
    'l_heel_loc': [9.01648766284925, 8.999999803973829, -3.0000015635754016],
    'l_indexFinger01_loc': [73.15209902861417, 148.77542132191334, 2.4571262793102715],
    'l_indexFinger02_loc': [75.89273002378945, 148.63085914848477, 2.3421963995873227],
    'l_indexFinger03_loc': [78.1703102134008, 147.8294824486201, 2.1581582564748674],
    'l_indexFingerNub_loc': [79.62771505903298, 146.42501754522584, 1.8998077823054957],
    'l_middleFinger01_loc': [73.29126684700238, 148.8662111031126, 0.802623353054483],
    'l_middleFinger02_loc': [75.84254391441976, 148.6544797715822, 0.23579633795882804],
    'l_middleFinger03_loc': [77.89045641693453, 147.8924250170955, -0.12400547314861737],
    'l_middleFingerNub_loc': [79.88455108582767, 146.25636204699148, -0.4738979650257093],
    'l_pinkyFinger01_loc': [72.23646492538126, 148.74823031808162, -2.396710983056597],
    'l_pinkyFinger02_loc': [73.66484017099772, 148.58410656969974, -3.10023485037732],
    'l_pinkyFinger03_loc': [75.41046093402618, 148.10249312563806, -3.9805551920552533],
    'l_pinkyFingerNub_loc': [76.65357905791906, 147.22575346795563, -4.701567751108401],
    'l_ringFinger01_loc': [72.9422449543394, 148.86300681701232, -0.8786873046811359],
    'l_ringFinger02_loc': [75.26585328047778, 148.66339099763337, -1.6219078896877046],
    'l_ringFinger03_loc': [77.22398316406374, 148.05818133059097, -2.315907070516789],
    'l_ringFingerNub_loc': [79.01784428586829, 146.54495173455706, -2.9546933552050803],
    'l_thigh_loc': [9.016487120738676, 103.21524918079396, -0.06317702051060863],
    'l_thumb01_loc': [70.11107543741674, 146.6170965926298, 3.5934129703622184],
    'l_thumb02_loc': [72.5774068262009, 145.94085720275243, 4.138805274033418],
    'l_thumbNub_loc': [74.20434461154682, 145.59246829389886, 4.010931396151761],
    'l_toeNub_loc': [9.016487800761242, 1.0000001203622366, 15.9999991785903],
    'l_toe_loc': [9.016487734626331, 1.0000008199679824, 4.999999178590323],
    'l_upperArm_loc': [13.000593001987955, 148.6553731643616, -0.46805473651793594],
    'neck01_loc': [-1.4730733192261448e-07, 155.10695179887028, -0.9901780366957804],
    'neck02_loc': [-2.1416909327475675e-07, 159.46418229884728, -1.8036069109735917],
    'pelvis_loc': [0.0, 105, 0.0],
    'root_loc': [0.0, 0.0, 0.0],
    'spine01_loc': [0.0, 111, 0.0],
    'spine02_loc': [0.0, 122.78129034666335, 2.591755210615142],
    'spine03_loc': [0.0, 138.25796503307137, -1.941777543511742],
    'spine04_loc': [0.0, 148.43186463177227, -3.0205814470408088]
}

thumbLocators = ['l_thumb01_loc', 'l_thumb02_loc', 'l_thumbNub_loc']
indexLocators = ['l_indexFinger01_loc', 'l_indexFinger02_loc', 'l_indexFinger03_loc', 'l_indexFingerNub_loc']
middleLocators = ['l_middleFinger01_loc', 'l_middleFinger02_loc', 'l_middleFinger03_loc', 'l_middleFingerNub_loc']
ringLocators = ['l_ringFinger01_loc', 'l_ringFinger02_loc', 'l_ringFinger03_loc', 'l_ringFingerNub_loc']
pinkyLocators = ['l_pinkyFinger01_loc', 'l_pinkyFinger02_loc', 'l_pinkyFinger03_loc', 'l_pinkyFingerNub_loc']
armLocators = ['l_clavicle_loc', 'l_clavicleNub_loc', 'l_upperArm_loc', 'l_foreArm_loc', 'l_hand_loc']
spineLocators = ['root_loc', 'COMOffset_loc', 'COM_loc', 'pelvis_loc', 'spine01_loc', 'spine02_loc', 'spine03_loc',
                 'spine04_loc', 'neck01_loc', 'neck02_loc', 'head01_loc', 'head02_loc', 'headNub_loc']
legLocators = ['l_thigh_loc', 'l_calf_loc', 'l_heel_loc', 'l_toe_loc', 'l_toeNub_loc']
eyeLocators = ['l_eye_loc', 'l_eyeNub_loc']
jawLocators = ['jaw_loc', 'jawNub_loc']

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

def spawnJoints2(list):                                                 #
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
    for i, j in locTemp.items():
        if i in list:
            cmds.joint(position=j, n=i + "_jnt")

#######################################################################################################################

def compareLists(list1, list2):                              # Compares a list to another and produces a new list in the same order
    newList = []                                             # like the first one out of the second one
    for i in list1:
         if i == list2[list2.index(i)]:
             newList.append(i)
    print(newList)

########################################################################################################################

def spawnTempLocators(args):                                                    # Create locators from  template dictionary
    for i, j in zip(locTemp.keys(), locTemp.values()):
        cmds.spaceLocator(position=j, name=i)

########################################################################################################################

def createDict():
    x = cmds.ls(type='locator')                             # Create dictionary from locators in the scene,  with locators'
    y = [i.replace('Shape', '') for i in x]
    locatorsDict = {}                                       # names as keys and their positions in space, as values.
    for i in y:                                             # Joints will be spawned from this dictionary
        position = cmds.pointPosition(i, world=True)
        locatorsDict[i] = position
    print(locatorsDict)
    return locatorsDict

########################################################################################################################

def spawnJoints(list, dict):                                # Create joints from list
    cmds.select(deselect=True)
    dict_keys = dict.keys()                                 # Creating dict list of keys from the dictionary

    list_B = []                                             # Converting it to regular list. This step is necessary, since
    for i in dict_keys:                                     # dict list is not iterable
        list_B.append(i)

    dictNew = {}                                            # Declaring the new list
    for i in list:                                          # For each item in list_A, if the item is in list_B
        if i in list_B:                                     # add it to the dictNew
            dictNew[i] = dict[i]                            # dictNew[item] becomes the key, = , dictOld[i] gets the
                                                            # corresponding values
    for i, j in dictNew.items():                            # Creating the chain by iterating over the keys and the values
        cmds.joint(position=j, n=i.replace('_loc', '_jnt')) # in the dictionary

    cmds.select(deselect=True)

    x = cmds.ls(type='locator')                             # Delete locators corresponding to the selected list
    y = [i.replace('Shape', '') for i in x]
    for i in y:
        if i in list:
            cmds.delete(i)

########################################################################################################################

allJoints = cmds.ls(type='joint')                                   # Convert suffix to prefix - UE mannequin

def prefixJoint(jointList, oldString, newString):                   # This function was used to rename UE mannequin
                                                                    # rig joints into more familiar convention  -
    for i in jointList:                                             # joint name starting with right/left position
        if oldString in i:                                          # and each bone with suffix '_jnt'
            cmds.rename(i, newString + i.replace(oldString, ''))


def renameAllJoints(jointList):                                     # Add '_jnt' suffix to all joints
    for i in jointList:
        cmds.rename(i, i + '_jnt')

prefixJoint(allJoints, '_r', 'r_')
prefixJoint(allJoints, '_l', 'l_')

allJoints = cmds.ls(type='joint')
renameAllJoints(allJoints)

########################################################################################################################

# jointList = cmds.ls(et="joint")                             # Creating template locators from given rig
                                                            # The function creates locators only for the left side                                                            # of the rig with the intention to be mirrored later
def removePrefix(list, prefix):                             # in the process
    for i in list:
        if prefix in i:
            list.remove(i)
            removePrefix(list)

removePrefix(jointList)

jointPosition = []
for i in jointList:
    jointPosition.append(cmds.xform(i, q=1, ws=1, rp=1))

y = []
for i in jointPosition:
    y.append(i)

locatorsList = []
for i, j in zip(jointPosition, jointList):
    locatorsList.append(cmds.spaceLocator(position=i, name=(j.replace("_jnt", "_loc"))))

x = []
for i in locatorsList:
    x.append(i[0])

namesValues = {}
nameValues = dict(zip(x, y))

for key, value in nameValues.items():
    print(key, ' : ', value)

########################################################################################################################

x = cmds.ls(sl=True)                                    # Change rotation order for the selected joint
for i in x:
    cmds.setAttr(i + '.rotateOrder', 0)

########################################################################################################################

x = cmds.ls(sl=True)                                    # Enable stretching for the selected joint
for i in x:
    cmds.setAttr(i + '.segmentScaleCompensate', 1)

########################################################################################################################

cmds.select(hi=True)                                    # Select hierarchy of the selected joint

########################################################################################################################

cmds.select(cmds.ls(et='joint'))                        # Select all joints

########################################################################################################################

cmds.joint(edit=True, zso=True)                        # Align translational axis to local rotational axis

########################################################################################################################

def setXYZp(args):
    a = cmds.radioButtonGrp(radioGroup1, q=True, sl=True)
    b = cmds.radioButtonGrp(radioGroup2, q=True, sl=True)
    if a == 1 and b == 1:
        cmds.radioButtonGrp(radioGroup2, e=True, sl=2)
    elif a == 2 and b == 2:
        cmds.radioButtonGrp(radioGroup2, e=True, sl=3)
    elif a == 3 and b == 3:
        cmds.radioButtonGrp(radioGroup2, e=True, sl=1)


def setXYZbs(args):
    a = cmds.radioButtonGrp(radioGroup1, q=True, sl=True)
    b = cmds.radioButtonGrp(radioGroup2, q=True, sl=True)
    if b == 1 and a == 1:
        cmds.radioButtonGrp(radioGroup1, e=True, sl=2)
    elif b == 2 and a == 2:
        cmds.radioButtonGrp(radioGroup1, e=True, sl=3)
    elif b == 3 and a == 3:
        cmds.radioButtonGrp(radioGroup1, e=True, sl=1)


def checkboxState(args):
    if cmds.checkBox(checkbox1, q=True, v=True) == 1:
        cmds.columnLayout(layout2, e=True, en=0)
    elif cmds.checkBox(checkbox1, q=True, v=True) == 0:
        cmds.columnLayout(layout2, e=True, en=1)


window = cmds.window(title="Spawn Joints", widthHeight=(600, 250))
layout1 = cmds.columnLayout(adjustableColumn=True, ebg=True)
checkbox1 = cmds.checkBox(label='Checkbox', value=0, onc=checkboxState, ofc=checkboxState)

layout2 = cmds.columnLayout(adjustableColumn=True, ebg=True)
radioGroup1 = cmds.radioButtonGrp(nrb=3, label='Primary Axis', labelArray3=['X', 'Y', 'Z'], sl=1, p=layout2, on1=setXYZp, on2=setXYZp, on3=setXYZp)
radioGroup2 = cmds.radioButtonGrp(nrb=4, label='Secondary Axis', labelArray4=['X', 'Y', 'Z', 'None'], sl=2, p=layout2, on1=setXYZbs, on2=setXYZbs, on3=setXYZbs)
radioGroup3 = cmds.radioButtonGrp(nrb=3, label='World Orientation', labelArray3=['X', 'Y', 'Z'], sl=2, p=layout2)

cmds.button(label='Do Nothing', command=checkboxState, parent=layout1)
cmds.button(label='Close', command=('cmds.deleteUI(\"' + window + '\", window=True)'), parent=layout1)

cmds.showWindow(window)

########################################################################################################################
#  FK controllers setup based on matrix

r1 = 1

jointList = cmds.ls(sl=True)  # Get list of selected joints
jointDict = {}  # Create dictionary with the names and positions of the selected joints
for i in jointList:
    jointDict[i] = cmds.xform(i, q=1, ws=1, rp=1)

ctrlList = []
for i, j in zip(jointDict.keys(), jointDict.values()):  # Create controllers, rename and position them on the joints

    cmds.xform(cmds.circle(n=i[:-4] + '_ctrl', r=7), t=j)
    ctrlList.append(i[:-4] + '_ctrl')  # Append controllers names to ctrlList
for i in ctrlList:
    if 'Finger' in i or 'thumb' in i:  # If the controller is a finger controller, set smaller radius
        cmds.circle(i, e=True, r=2)

if r1 == 1:
    for i in ctrlList:
        cmds.circle(i, e=True,
                    nr=[1, 0, 0])  # Set normal orientation for the controllers based on primary axis orientation
elif r1 == 2:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 1, 0])
elif r1 == 3:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 0, 1])

for i, j in zip(ctrlList, jointList):  # Match rotations of the controller to the rotation of the respective joint
    cmds.matchTransform(i, j, rot=True)

ctrlList.reverse()  # Reverse list so each item can be parented to the next one in the list
for i in ctrlList:  #
    index = ctrlList.index(i)
    cmds.parent(ctrlList[index], ctrlList[index + 1])
    if index == len(ctrlList) - 2:  # When the loop gets to the last index, break to avoid index out of range error
        break
cmds.select(deselect=True)
ctrlList.reverse()


for i, j in zip(ctrlList, jointList):
    cmds.setAttr(i + '.offsetParentMatrix', tuple(cmds.getAttr(i + '.xformMatrix')), type='matrix')  # Copy all values from transform attributes to Offset Parent Matrix
    # This way the values can be zeroed and the controller remains clean
    cmds.setAttr(i + '.translate', 0, 0, 0, type='double3')  # Zero out translation and rotation (scale and shear should be already zeroed)
    cmds.setAttr(i + '.rotate', 0, 0, 0, type='double3')
    cmds.select(deselect=True)
    cmds.connectAttr(i + '.worldMatrix[0]', j + '.offsetParentMatrix', force=True)  # Connect controllers world matrix to OPM
    cmds.setAttr(j + '.translate', 0, 0, 0, type='double3')  # Zero out translation and orientation on the joint
    cmds.setAttr(j + '.jointOrient', 0, 0, 0, type='double3')
    if ctrlList.index(i) > 0:  # The second and the following controllers need to account for the values of the parent, so another node to offset them is needed
        mm1 = cmds.shadingNode('multMatrix', asUtility=True, name='multM_'+j[:-4])  # Create multMatrix node and rename it. This node will blend the values and pass them on
        cmds.connectAttr(i + '.worldMatrix[0]', mm1 + '.matrixIn[0]', force=True)  # Connect world matrix[0] of the controller to matrixIn[0] of the blend node
        cmds.connectAttr(jointList[jointList.index(j)-1] + '.parentInverseMatrix', mm1 + '.matrixIn[1]', force=True)  # Connect the root joint's parent inverse matrix
        # to matrixIn[1] to offset parents matrix values, that way taking the hierarchy into account
        cmds.connectAttr(mm1 + '.matrixSum', j + '.offsetParentMatrix', force=True)  # Connect matrixSum from the blend matrix node to next joint OPM

########################################################################################################################

#  FK/IK school Setup

r1 = 1

jointList = cmds.ls(sl=True)  # Get list of selected joints
jointDict = {}  # Create dictionary with the names and positions of the selected joints
for i in jointList:
    jointDict[i] = cmds.xform(i, q=1, ws=1, rp=1)

ctrlList = []
for i, j in zip(jointDict.keys(), jointDict.values()):  # Create controllers, rename and position them on the joints

    cmds.xform(cmds.circle(n=i[:-4] + '_ctrl', r=7), t=j)
    ctrlList.append(i[:-4] + '_ctrl')  # Append controllers names to ctrlList
for i in ctrlList:
    if 'Finger' in i or 'thumb' in i:  # If the controller is a finger controller, set smaller radius
        cmds.circle(i, e=True, r=2)

if r1 == 1:
    for i in ctrlList:
        cmds.circle(i, e=True,
                    nr=[1, 0, 0])  # Set normal orientation for the controllers based on primary axis orientation
elif r1 == 2:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 1, 0])
elif r1 == 3:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 0, 1])

for i, j in zip(ctrlList, jointList):  # Match rotations of the controller to the rotation of the respective joint

    cmds.parent(i, j)                   # Parent each controller to each joint
    cmds.matchTransform(i, j, rot=True)  # Match transformations
    cmds.makeIdentity(apply=True)  # Freeze transformations
    cmds.delete(i, ch=True)  # Delete construction history
    cmds.select(i + 'Shape')  # Select shape node
    cmds.select(j, add=True)    # Add respective joint to the selection. Order of selection is important for this to work
    cmds.parent(s=True, r=True)  # Parent the shape node
    cmds.delete(i)  # Delete the transform node
cmds.ikHandle(startJoint='arm_jnt', endEffector='hand_jnt')  # Create IK handle
cmds.xform(cmds.circle(n='ik_ctrl', r=10, nr=[1, 0, 0]), t=cmds.xform(jointList[2], q=1, ws=1, rp=1))  # Create IK controller and position it on the joint
cmds.parent('ikHandle1', 'ik_ctrl')  # Parent the handle to the control

########################################################################################################################

#  FK/IK Setup Python 2.x

r1 = 1

jointList = cmds.ls(sl=True)  # Get list of selected joints
jointPositions = []
for i in jointList:
    jointPositions.append(cmds.xform(i, q=1, ws=1, rp=1))

ctrlList = []
for i, j in zip(jointList, jointPositions):  # Create controllers, rename and position them on the joints

    cmds.xform(cmds.circle(n=i[:-4] + '_ctrl', r=7), t=j)
    ctrlList.append(i[:-4] + '_ctrl')  # Append controllers names to ctrlList
for i in ctrlList:
    if 'Finger' in i or 'thumb' in i:  # If the controller is a finger controller, set smaller radius
        cmds.circle(i, e=True, r=2)

if r1 == 1:
    for i in ctrlList:
        cmds.circle(i, e=True,
                    nr=[1, 0, 0])  # Set normal orientation for the controllers based on primary axis orientation
elif r1 == 2:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 1, 0])
elif r1 == 3:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 0, 1])

for i, j in zip(ctrlList, jointList):  # Match rotations of the controller to the rotation of the respective joint

    cmds.parent(i, j)                   # Parent each controller to each joint
    cmds.matchTransform(i, j, rot=True)  # Match transformations
    cmds.makeIdentity(apply=True)  # Freeze transformations
    cmds.delete(i, ch=True)  # Delete construction history
    cmds.select(i + 'Shape')  # Select shape node
    cmds.select(j, add=True)    # Add respective joint to the selection. Order of selection is important for this to work
    cmds.parent(s=True, r=True)  # Parent the shape node
    cmds.delete(i)  # Delete the transform node
cmds.ikHandle(startJoint=jointList[0], endEffector=jointList[2])  # Create IK handle
cmds.xform(cmds.circle(n='ik_ctrl', r=10, nr=[1, 0, 0]), t=cmds.xform(jointList[2], q=1, ws=1, rp=1))  # Create IK controller and position it on the joint
cmds.parent('ikHandle1', 'ik_ctrl')  # Parent the handle to the control

########################################################################################################################

# FK chain with group controls and constraints

def rope(numberOfJoints, spaceBetween, alongAxis, controllersRadius, step):
    index = 0
    jointList = []
    for i in range(numberOfJoints):
        if alongAxis is 'x':
            jointList.append(cmds.joint(name='joint_' + str(i + 1) + '_jnt', position=[index, 0, 0]))
        elif alongAxis is 'y':
            jointList.append(cmds.joint(name='joint_' + str(i + 1) + '_jnt', position=[0, index, 0]))
        elif alongAxis is 'z':
            jointList.append(cmds.joint(name='joint_' + str(i + 1) + '_jnt', position=[0, 0, index]))
        index += spaceBetween

    jointPositions = []
    jointStep = []
    for i in range(0, len(jointList) - 1, step):
        jointPositions.append(cmds.xform(jointList[i], query=True, worldSpace=True, rotatePivot=True))
        jointStep.append(jointList[i])

    ctrlList = []
    for i, j in zip(jointStep, jointPositions):  # Create controllers, rename and position them on the joints
        cmds.xform(cmds.circle(name=i[:-4] + '_ctrl', radius=controllersRadius), translation=j)
        ctrlList.append(i[:-4] + '_ctrl')
    for i in ctrlList:
        if alongAxis is 'x':
            cmds.circle(i, edit=True, normal=[1, 0,
                                              0])  # Set normal orientation for the controllers based on primary axis orientation
        elif alongAxis is 'y':
            cmds.circle(i, edit=True, normal=[0, 1, 0])
        elif alongAxis is 'z':
            cmds.circle(i, edit=True, normal=[0, 0, 1])

    offsetList = []
    for i, j in zip(ctrlList, jointStep):
        offsetList.append(cmds.group(i, name=i[:-4] + 'offset'))  # Group each controller and add the name to a list

    for i, j, o in zip(ctrlList, jointStep, offsetList):
        cmds.matchTransform(o, j)
        cmds.makeIdentity(o, apply=True, translate=True)  # Freeze transformations
        cmds.makeIdentity(i, apply=True)  # Freeze transformations
        cmds.delete(i, constructionHistory=True)  # Delete construction history
        cmds.parentConstraint(i, j, maintainOffset=True)  # Constrain joints to controls

    for i, j in zip(ctrlList[:-1], offsetList[:-1]):  #
        offset = offsetList[offsetList.index(j) + 1]
        ctrl = ctrlList[ctrlList.index(i)]
        cmds.parent(offset, ctrl)  # Parent controls under each other

    for i in ctrlList:
        for j in jointList:
            if i[:-4] in j:
                for each in range(step):
                    cmds.connectAttr(i + '.rotate', jointList[jointList.index(j) + each] + '.rotate', force=True)

    for i, j in zip(jointStep[1:], offsetList[1:]):
        if i in jointList:
            cmds.parentConstraint(jointList[jointList.index(i) - 1], j, mo=True, w=1)


rope(15, 10, 'y', 5, 3)

########################################################################################################################

# FK chain for the hand with group controls and constraints

r1 = 1  # radio button, containing the selected axis (x,y,z); based on that, the controls are spawned with normals pointing in the same direction

jointList = cmds.ls(sl=True)  # Get list of selected joints
jointPositions = []
for i in jointList:
    jointPositions.append(cmds.xform(i, q=1, ws=1, rp=1))

ctrlList = []
for i, j in zip(jointList, jointPositions):  # Create controllers, rename and position them on the joints

    cmds.xform(cmds.circle(n=i[:-4] + '_ctrl', r=7), t=j)
    ctrlList.append(i[:-4] + '_ctrl')  # Append controllers names to ctrlList

for i in ctrlList:
    if 'Finger' in i or 'thumb' in i:  # If the controller is a finger controller, set smaller radius
        cmds.circle(i, e=True, r=2)

if r1 == 1:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[1, 0, 0])  # Set normal orientation for the controllers based on primary axis orientation
elif r1 == 2:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 1, 0])
elif r1 == 3:
    for i in ctrlList:
        cmds.circle(i, e=True, nr=[0, 0, 1])

offsetList = []
for i, j in zip(ctrlList, jointList):
    offsetList.append(cmds.group(i, name=i[:-4] + 'offset'))  # Group each controller and add the name to a list

for i, j, o in zip(ctrlList, jointList, offsetList):
    cmds.matchTransform(o, j)
    cmds.makeIdentity(o, apply=True, translate=True)  # Freeze transformations
    cmds.makeIdentity(i, apply=True)  # Freeze transformations
    cmds.delete(i, constructionHistory=True)  # Delete construction history
    cmds.parentConstraint(i, j, maintainOffset=True)  # Constrain joints to controls

for i, j in zip(ctrlList[:-1], offsetList[:-1]):  #
    offset = offsetList[offsetList.index(j) + 1]
    ctrl = ctrlList[ctrlList.index(i)]
    cmds.parent(offset, ctrl)  # Parent controls under each other

for i in offsetList[:-1]:  # Parent fingers controls. If 'Nub' is in item (as in, 'i' is the last joint in the hierarchy),
    if 'Nub' in offsetList[offsetList.index(i)]:
        cmds.parent(offsetList[offsetList.index(i) + 1], 'l_hand_ctrl')  # parent next item under l_hand_ctrl

########################################################################################################################