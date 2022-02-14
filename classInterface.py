import maya.cmds as cmds


class GUI:

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

    handLocators = [thumbLocators, indexLocators, middleLocators, ringLocators, pinkyLocators]
    allLists = [armLocators, legLocators, spineLocators, eyeLocators, jawLocators, thumbLocators,
                indexLocators, middleLocators, ringLocators, pinkyLocators]
    allChains = [armLocators, legLocators, spineLocators, eyeLocators, jawLocators, handLocators, allLists]

    def __init__(self):

        self.window = 'MyWindow'
        self.title = 'Rigging Tools'
        self.size = (400, 400)

    def spawnTempLocators(self):
        for i, j in zip(GUI.locTemp.keys(),
                        GUI.locTemp.values()):                      # Create locators from template dictionary
            cmds.spaceLocator(position=j, name=i)

    def spawnJoints(self, slist):                                   # Create joints from list

        x = cmds.ls(type='locator', s=False)                                 # Create dictionary from locators in the scene,  with locators'
        y = [i.replace('Shape', '') for i in x]
        locatorsDict = {}                                           # names as keys and their positions in space, as values.
        for i in y:                                                 # Joints will be spawned from this dictionary
            position = cmds.pointPosition(i, world=True)
            locatorsDict[i] = position

        cmds.select(deselect=True)
        dictKeys = locatorsDict.keys()                             # Creating dict list of keys from the dictionary

        list_B = []                                                 # Converting it to regular list. This step is necessary, since
        for i in dictKeys:                                         # dict list is not iterable
            list_B.append(i)

        dictNew = {}                                                # Declaring the new list
        for i in slist:                                             # For each item in list_A, if the item is in list_B
            if i in list_B:                                         # add it to the dictNew
                dictNew[i] = locatorsDict[i]                        # dictNew[item] becomes the key, = , dictOld[i] gets the corresponding values

        for i, j in dictNew.items():                                # Creating the chain by iterating over the keys and the values
            cmds.joint(n=i.replace('_loc', '_jnt'), position=j)     # in the dictionary

        cmds.select(deselect=True)

        orientJoints = cmds.ls(type='joint')
        print(orientJoints)                                         # Orient all joints
        cmds.joint(orientJoints[0], e=True, oj='xyz', sao='zup', ch=True, zso=True)


        confirmMessage = cmds.confirmDialog(title='Confirm', message='Delete corresponding locators?', button=['Yes', 'No'],
                                            defaultButton='Yes', cancelButton='No', dismissString='No')
        if confirmMessage == 'Yes':
            for i in slist:
                cmds.delete(i)

    def displayLocalAxis(self):                                         # Display local orientation axis
        jointList = cmds.ls(type='joint')
        selection = cmds.ls(sl=True)
        for i in selection:
            if i in jointList:
                if not cmds.getAttr(i + '.displayLocalAxis'):
                    cmds.setAttr(i + '.displayLocalAxis', 1)
                else:
                    cmds.setAttr(i + '.displayLocalAxis', 0)

    def deleteAllLocators(self):

        locators = [each.replace('Shape', '') for each in cmds.ls(type='locator')]
        for each in locators:
            cmds.delete(each)

    def selectJointChain(self):
        selected = cmds.optionMenuGrp('optMenu', query=True, sl=True) - 1
        dropdownList = GUI.allChains[int(selected)]

        if isinstance(dropdownList[0], list):                       # If selected list contains list (like handLoc)
            for i in dropdownList:                                  # execute for each sublist
                GUI.spawnJoints(self, i)
        else:                                                       # else execute list
            GUI.spawnJoints(self, dropdownList)

    def windowFunction(self):
        if cmds.window(self.window, query=True, exists=True):
            cmds.deleteUI(self.window)

        cmds.window(self.window, title=self.title, widthHeight=self.size)
        cmds.columnLayout(adjustableColumn=True, ebg=True)

        tabs = cmds.tabLayout(bs='none')

        tab1 = cmds.columnLayout(adjustableColumn=True, ebg=True)
        cmds.separator(height=10, st='none')
        cmds.optionMenuGrp('optMenu', label='Create Joint Chain')
        cmds.separator(height=10, st='none')
        cmds.menuItem(label='Arm')
        cmds.menuItem(label='Leg')
        cmds.menuItem(label='Spine')
        cmds.menuItem(label='Eyes')
        cmds.menuItem(label='Jaw')
        cmds.menuItem(label='Hand')
        cmds.menuItem(label='All chains')
        cmds.separator(height=2, st='none')
        cmds.button(label='Spawn Locators', command=GUI.spawnTempLocators, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Spawn Joints', command=GUI.selectJointChain, height=30)

        cmds.setParent('..')

        tab2 = cmds.columnLayout(adjustableColumn=True, ebg=True)
        cmds.separator(height=2, st='none')
        cmds.button(label='Display Local Orientation Axis', command=GUI.displayLocalAxis, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Delete All Locators', command=GUI.deleteAllLocators, height=30)
        cmds.setParent('..')

        cmds.tabLayout(tabs, edit=True, tabLabel=((tab1, 'Main'), (tab2, 'Misc')))

        cmds.showWindow()


myWindow = GUI()
myWindow.windowFunction()
