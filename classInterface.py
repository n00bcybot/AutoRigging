import maya.cmds as cmds


class GUI:

    unreal_mannequinn = {

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
