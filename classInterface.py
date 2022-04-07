import maya.cmds as cmds
import maya.OpenMaya as om


# noinspection PyUnusedLocal
def displayLocalAxis(args):  # Display local orientation axis

    selection = cmds.ls(sl=True)
    for i in selection:
        if not cmds.getAttr(i + '.displayLocalAxis'):
            cmds.setAttr(i + '.displayLocalAxis', 1)
        else:
            cmds.setAttr(i + '.displayLocalAxis', 0)


# noinspection PyUnusedLocal
def deleteAllLocators(args):
    locators = [each.replace('Shape', '') for each in cmds.ls(type='locator')]
    for each in locators:
        cmds.delete(each)


# noinspection PyUnusedLocal
def selectAllJoints(args):
    cmds.select(cmds.ls(et='joint'))  # Select all joints in the scene


# noinspection PyUnusedLocal
def selectHierarchy(args):
    cmds.select(hi=True)  # Select hierarchy of the selected joint


# noinspection PyUnusedLocal
def disableScaleComp(args):  # Disable/enable scale compensate for stretchy joints
    jointList = cmds.ls(type='joint')
    selection = cmds.ls(sl=True)
    for i in selection:
        if i in jointList:
            if not cmds.getAttr(i + '.segmentScaleCompensate'):
                cmds.setAttr(i + '.segmentScaleCompensate', 1)
            else:
                cmds.setAttr(i + '.segmentScaleCompensate', 0)


# noinspection PyUnusedLocal
def changeRotationOrder(args):
    jointList = cmds.ls(sl=True)  # Change rotation order for the selected joint
    selection = cmds.optionMenuGrp('rotationMenu', query=True, sl=True) - 1
    for each in jointList:
        cmds.setAttr(each + '.rotateOrder', int(selection))


# noinspection PyUnusedLocal
def alignTransAxis(args):       # Aligning translation axis', in case they have been rotated, for the thumb for example
    x = cmds.ls(sl=True)
    for i in x:
        cmds.joint(i, edit=True, zso=True)


# noinspection PyUnusedLocal
def parentFingers(args):
    y = []                                          # Parent all fingers to hand joint
    for each in Interface.l_fingerLocators:
        y.append(each[0].replace('_loc', '_jnt'))
    for i in y:
        cmds.parent(i, 'l_hand_jnt')
        cmds.select(deselect=True)


# noinspection PyUnusedLocal
def unparentFingers(args):
    y = []                                          # Parent all fingers to hand joint
    for each in Interface.l_fingerLocators:
        y.append(each[0].replace('_loc', '_jnt'))
    for i in y:
        cmds.parent(i, w=True)
        cmds.select(deselect=True)


# noinspection PyUnusedLocal
def matchAllTransform(args):
    cmds.matchTransform(cmds.ls(sl=True)[0], cmds.ls(sl=True)[1])


# noinspection PyUnusedLocal
def changeShapeColor(itemName, color):

    cmds.select(itemName)
    shapeNode = cmds.listRelatives(s=True)[0]
    cmds.setAttr(shapeNode + ".overrideEnabled", 1)  # Change locators' color
    cmds.setAttr(shapeNode + ".overrideColor", color)  # to yellow


# noinspection PyUnusedLocal
def resetControls(args):

    left = 'l_'
    right = 'r_'

    nurbs = cmds.ls(et='nurbsCurve')
    selection = cmds.ls(sl=True)

    side = []
    for i in nurbs:
        if selection[0] in i:
            if left in i:
                side = left
            elif right in i:
                side = right

    ctrlList = [side + 'upperArm_FK_ctrl', side + 'foreArm_FK_ctrl', side + 'hand_FK_ctrl', side + 'arm_ikHandle_ctrl', side + 'elbow_ctrl']
    xyz = ['X', 'Y', 'Z']
    for i in ctrlList:
        for j in xyz:
            cmds.setAttr(i + '.rotate' + j, 0)
            cmds.setAttr(i + '.translate' + j, 0)


# noinspection PyUnusedLocal
def mirrorJoints(joint):
    cmds.mirrorJoint(joint, mirrorYZ=True, mirrorBehavior=True, searchReplace=('l_', 'r_'))


# noinspection PyUnusedLocal
class Interface:

    unrealMannequin = {

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

### L locators

    l_thumbLocators = ['l_thumb01_loc', 'l_thumb02_loc', 'l_thumbNub_loc']
    l_indexLocators = ['l_indexFinger01_loc', 'l_indexFinger02_loc', 'l_indexFinger03_loc', 'l_indexFingerNub_loc']
    l_middleLocators = ['l_middleFinger01_loc', 'l_middleFinger02_loc', 'l_middleFinger03_loc', 'l_middleFingerNub_loc']
    l_ringLocators = ['l_ringFinger01_loc', 'l_ringFinger02_loc', 'l_ringFinger03_loc', 'l_ringFingerNub_loc']
    l_pinkyLocators = ['l_pinkyFinger01_loc', 'l_pinkyFinger02_loc', 'l_pinkyFinger03_loc', 'l_pinkyFingerNub_loc']
    l_armLocators = ['l_clavicle_loc', 'l_upperArm_loc', 'l_foreArm_loc', 'l_hand_loc']
    spineLocators = ['root_loc', 'COMOffset_loc', 'COM_loc', 'pelvis_loc', 'spine01_loc', 'spine02_loc', 'spine03_loc',
                     'spine04_loc', 'neck01_loc', 'neck02_loc', 'head01_loc', 'head02_loc', 'headNub_loc']
    l_legLocators = ['l_thigh_loc', 'l_calf_loc', 'l_heel_loc', 'l_toe_loc', 'l_toeNub_loc']
    l_eyeLocators = ['l_eye_loc', 'l_eyeNub_loc']
    jawLocators = ['jaw_loc', 'jawNub_loc']

    l_ikJoints = ['l_upperArm_IK_jnt', 'l_foreArm_IK_jnt', 'l_hand_IK_jnt']
    l_fkJoints = ['l_upperArm_FK_jnt', 'l_foreArm_FK_jnt', 'l_hand_FK_jnt']
    l_armJoints = ['l_upperArm_jnt', 'l_foreArm_jnt', 'l_hand_jnt']

### R locators

    r_thumbLocators = ['r_thumb01_loc', 'r_thumb02_loc', 'r_thumbNub_loc']
    r_indexLocators = ['r_indexFinger01_loc', 'r_indexFinger02_loc', 'r_indexFinger03_loc', 'r_indexFingerNub_loc']
    r_middleLocators = ['r_middleFinger01_loc', 'r_middleFinger02_loc', 'r_middleFinger03_loc', 'r_middleFingerNub_loc']
    r_ringLocators = ['r_ringFinger01_loc', 'r_ringFinger02_loc', 'r_ringFinger03_loc', 'r_ringFingerNub_loc']
    r_pinkyLocators = ['r_pinkyFinger01_loc', 'r_pinkyFinger02_loc', 'r_pinkyFinger03_loc', 'r_pinkyFingerNub_loc']

    r_fingerLocators = [r_thumbLocators, r_indexLocators, r_middleLocators, r_ringLocators, r_pinkyLocators]

    r_ikJoints = ['r_upperArm_IK_jnt', 'r_foreArm_IK_jnt', 'r_hand_IK_jnt']
    r_fkJoints = ['r_upperArm_FK_jnt', 'r_foreArm_FK_jnt', 'r_hand_FK_jnt']
    r_armJoints = ['r_upperArm_jnt', 'r_foreArm_jnt', 'r_hand_jnt']

### Global locators

    l_fingerLocators = [l_thumbLocators, l_indexLocators, l_middleLocators, l_ringLocators, l_pinkyLocators]
    l_handLocators = [l_armLocators, l_thumbLocators, l_indexLocators, l_middleLocators, l_ringLocators, l_pinkyLocators]

    allLists = [l_armLocators, l_legLocators, spineLocators, l_eyeLocators, jawLocators, l_thumbLocators,
                l_indexLocators, l_middleLocators, l_ringLocators, l_pinkyLocators]
    allChains = [l_handLocators, l_legLocators, spineLocators, l_eyeLocators, jawLocators, allLists]

### Switches

    switchCtrlPoints = [(0, 0, 0), (2, 0, -2), (2, 0, -1), (6, 0, -1), (6, 0, -2), (8, 0, 0), (6, 0, 2), (6, 0, 1), (2, 0, 1), (2, 0, 2), (0, 0, 0)]
    switchCtrlPCount = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    normal = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    def __init__(self):

        self.window = 'MyWindow'
        self.title = 'Rigging Tools'
        self.size = (400, 400)

        if cmds.window(self.window, query=True, exists=True):
            cmds.deleteUI(self.window)

        self.mainWindow = cmds.window(self.window, title=self.title, widthHeight=self.size)
        self.mainLayout = cmds.columnLayout(adjustableColumn=True, ebg=True, parent=self.mainWindow)

        self.tabs = cmds.tabLayout(bs='none', parent=self.mainLayout)

        self.tab1 = cmds.columnLayout(adjustableColumn=True, ebg=True, parent=self.tabs)
        cmds.separator(height=10, st='none')
        cmds.optionMenuGrp('optMenu', label='Create Joint Chain')
        cmds.separator(height=10, st='none')
        cmds.menuItem(label='Arm')
        cmds.menuItem(label='Leg')
        cmds.menuItem(label='Spine')
        cmds.menuItem(label='Eyes')
        cmds.menuItem(label='Jaw')
        cmds.menuItem(label='All chains')

        cmds.separator(height=2, st='none')
        cmds.button(label='Spawn Locators', command=self.spawnTempLocators, height=30)
        cmds.separator(height=2, st='none')

        self.layout1 = cmds.columnLayout(adjustableColumn=True, ebg=True, parent=self.tab1)
        self.layout3 = cmds.columnLayout(parent=self.layout1, cw=470, cat=('both', 142))

        self.checkbox1 = cmds.checkBox(label='Orient Joint To World', value=0, onc=self.checkboxState, ofc=self.checkboxState, parent=self.layout3)
        self.layout2 = cmds.columnLayout(adjustableColumn=True, ebg=True, parent=self.layout1)
        self.radioGroup1 = cmds.radioButtonGrp(nrb=3, label='Primary Axis', labelArray3=['X', 'Y', 'Z'], cw=([2, 70], [3, 70]), sl=1, p=self.layout2, on1=self.setXYZp, on2=self.setXYZp, on3=self.setXYZp)
        self.radioGroup2 = cmds.radioButtonGrp(nrb=4, label='Secondary Axis', labelArray4=['X', 'Y', 'Z', 'None'], cw=([2, 70], [3, 70], [4, 70]), sl=2, p=self.layout2, on1=self.setXYZs, on2=self.setXYZs, on3=self.setXYZs, on4=self.noneChecked, of4=self.noneUnchecked)
        self.radioGroup3 = cmds.radioButtonGrp(nrb=3, label='SA World Orientation', labelArray3=['X', 'Y', 'Z'], cw=([2, 70], [3, 70], [4, 70]), sl=2, p=self.layout2)

        cmds.optionMenuGrp('updown', parent=self.radioGroup3)
        cmds.menuItem(label='+')
        cmds.menuItem(label='-')

        cmds.separator(height=2, st='none')
        cmds.button(label='Spawn Joints', p=self.tab1, command=self.createJointChain, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Orient Joints', p=self.tab1, command=self.orientJoints, height=30)

        cmds.separator(height=2, st='none')
        cmds.button(label='Match Transformations', p=self.tab1, command=matchAllTransform, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Create FK Controls', p=self.tab1, command=self.createFKcontrols, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Create IK Controls', p=self.tab1, command=self.createIKcontrols, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Duplicate Joints', p=self.tab1, command=self.duplicateJoints, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Snap FK to IK / IK to FK', p=self.tab1, command=self.snapIKFK, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Reset Controls', p=self.tab1, command=resetControls, height=30)

        self.tab2 = cmds.columnLayout(adjustableColumn=True, ebg=True, parent=self.tabs)
        cmds.separator(height=2, st='none')
        cmds.button(label='Display/Hide Local Orientation Axis', command=displayLocalAxis, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Delete All Locators', command=deleteAllLocators, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Select All Joints', command=selectAllJoints, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Select Hierarchy', command=selectHierarchy, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Disable/Enable Scale Compensation', command=disableScaleComp, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Set Rotation Order', command=changeRotationOrder, height=30)

        cmds.separator(height=10, st='none')
        cmds.optionMenuGrp('rotationMenu', label='Select Order:')
        cmds.separator(height=10, st='none')
        cmds.menuItem(label='xyz')
        cmds.menuItem(label='yzx')
        cmds.menuItem(label='zxy')
        cmds.menuItem(label='xzy')
        cmds.menuItem(label='yxz')
        cmds.menuItem(label='zyx')

        cmds.separator(height=2, st='none')
        cmds.button(label='Align Translational Axis To Local Rotational Axis', command=alignTransAxis, height=30)

        cmds.tabLayout(self.tabs, edit=True, tabLabel=((self.tab1, 'Main'), (self.tab2, 'Misc')))

        cmds.showWindow()

    def spawnTempLocators(self, args):
        x = cmds.ls(type='locator', s=False)
        y = [i.replace('Shape', '') for i in x]

        for i, j in zip(self.locTemp.keys(), self.locTemp.values()):  # Create locators from template dictionary
            if i not in y:
                cmds.spaceLocator(position=j, name=i)
                cmds.xform(cp=True)
                cmds.setAttr(i + 'Shape' + ".overrideEnabled", 1)  # Change locators' color
                cmds.setAttr(i + 'Shape' + ".overrideColor", 17)  # to yellow
            else:
                i = None

        cmds.select(deselect=True)

    @staticmethod
    def spawnJoints(slist):  # Create joints from list

        x = cmds.ls(type='locator', s=False)  # Create dictionary from locators in the scene,  with locators'
        y = [i.replace('Shape', '') for i in x]
        locatorsDict = {}  # names as keys and their positions in space, as values.
        for i in y:  # Joints will be spawned from this dictionary
            position = cmds.pointPosition(i, world=True)
            locatorsDict[i] = position

        dictKeys = locatorsDict.keys()  # Creating dict list of keys from the dictionary

        list_B = []  # Converting it to regular list. This step is necessary, since
        for i in dictKeys:  # dict list is not iterable
            list_B.append(i)

        dictNew = {}  # Declaring the new list
        for i in slist:  # For each item in slist, if the item is in list_B
            if i in list_B:  # add it to the dictNew
                dictNew[i] = locatorsDict[i]  # dictNew[item] becomes the key, = , dictOld[i] gets the corresponding values

        jointList = []
        for i, j in dictNew.items():  # Creating the chain by iterating over the keys and the values

            cmds.joint(n=i.replace('_loc', '_jnt'), position=j)  # in the dictionary
            jointList.append(i.replace('_loc', '_jnt'))  # This line appends a list with joint names, which further down is used

        cmds.select(deselect=True)                      # to select the first joint from the list, after the joints are created.
        cmds.select(jointList[0].replace('_loc', '_jnt'))  # The selected joint is used then to orient the joints along the chain.

        # confirmMessage = cmds.confirmDialog(title='Confirm', message='Delete corresponding locators?', button=['Yes', 'No'],
        #                                     defaultButton='Yes', cancelButton='No', dismissString='No')
        # if confirmMessage == 'Yes':
        for i in slist:
            cmds.delete(i)

    def orientJoints(self, args):

        def findNub():  # This function checks whether the joint that needs to be orientated is at the end of the chain, as in, it has no children
            # If it has no children, it will oriented to the world (meaning it will inherit orientation from the parent joint)
            for each in orient:     # thus automatically aligning correctly
                if cmds.listRelatives(each) is None:
                    cmds.joint(each, e=True, oj='none', ch=True, zso=True)
                else:
                    cmds.joint(each, e=True, oj=allAxis, sao=secAxis, ch=True, zso=True)

        xyz = ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx']  # List with all possible combinations for primary axis orientation
        a = ['x', 'y', 'z']
        b = ['up', 'down']

        r1 = cmds.radioButtonGrp(self.radioGroup1, query=True, sl=True)
        r2 = cmds.radioButtonGrp(self.radioGroup2, query=True, sl=True)
        r3 = cmds.radioButtonGrp(self.radioGroup3, query=True, sl=True)
        r4 = cmds.optionMenuGrp('updown', query=True, sl=True)

        sel = a[r1 - 1] + a[r2 - 1]  # Querying the radio buttons and setting the desired axis from list 'a'
        allAxis = ''                # The radio buttons produce integers that correspond to the letters of each radio button
        for i in xyz:               # The corresponding letters are then taken from list 'a', concatenated and compared against
            if sel in i[:2]:        # list 'xyz'. The matching string is assigned to 'allAxis', which defines the orientation
                allAxis = i         # of the primary axis

        secAxis = a[r3 - 1] + b[r4 - 1]  # Querying r3 and b to establish orientation for the secondary axis

        cmds.select(hi=True)    # Selecting all joints in the hierarchy
        orient = cmds.ls(sl=True)  # and storing their names in here
        findNub()
        if 'l_hand_jnt' in orient:  # Checking if 'l_hand_jnt' is in the list of joints, if so, the fingers need to be unparented
            unparentFingers(args=True)  # and then orientated. If they are not, the wrist will be oriented towards the next joint

        c = []                           # that is created (the thumb), which is wrong in the case of the hand. Rather, it needs to
        for i in orient:                        # be aligned with the elbow (the world) - that can only happen if it has no children.
            c.append(cmds.joint(i, q=True, o=True))  # Creating the joints and a list with their orientations
        for i in c:                                 # if any of the xyz orientations equals 180, it means the joint has flipped
            for j in i:                             # the following code corrects that with setting the appropriate secondary axis orientation
                if round(j) == 180:
                    if cmds.xform(orient[1], q=1, ws=1, rp=1)[0] > cmds.xform(orient[0], q=1, ws=1, rp=1)[0]:  # If X value on the second joint in the hierarchy
                        if r3 == 3:                                                                            # is greater than X value of the first joint:
                            secAxis = a[r3 - 1] + b[r4 - 1]
                        else:
                            secAxis = a[r3 - 3] + b[r4 - 1]
                    if cmds.xform(orient[1], q=1, ws=1, rp=1)[1] > cmds.xform(orient[0], q=1, ws=1, rp=1)[1]:  # If Y value on the second joint in the hierarchy
                        if r3 == 3:                                                                            # is greater than Y value of the first joint:
                            secAxis = a[r3 - 1] + b[r4 - 1]
                        else:
                            secAxis = a[r3 - 2] + b[r4 - 1]
        findNub()
        if 'l_hand_jnt' in orient:
            parentFingers(args=True)  # Parents the fingers back

    def createJointChain(self, args):
        selected = cmds.optionMenuGrp('optMenu', query=True, sl=True) - 1  # Querying the dropdown menu
        dropdownList = self.allChains[int(selected)]  # Getting the respective list form allChains

        if isinstance(dropdownList[0], list):  # If selected list contains list (like handLoc)
            for i in dropdownList:  # execute for each sublist
                self.spawnJoints(i)

        else:  # else execute list
            self.spawnJoints(dropdownList)

        if isinstance(dropdownList[0], list):  # This part selects the first joint in the hierarchy, so it can orientate it with the function further down
            cmds.select(dropdownList[0][0].replace('_loc', '_jnt'))
        else:
            cmds.select(dropdownList[0].replace('_loc', '_jnt'))
        Interface.orientJoints(self, args=True)

    def duplicateJoints(self, args):

        def duplicateChain(chain, armChain):

            def jointPosition():
                jointPositions = []
                for each in armChain:
                    jointPositions.append(cmds.xform(each, q=1, ws=1, rp=1))
                return jointPositions

            for i, j in zip(chain, jointPosition()):
                cmds.joint(n=i, position=j)
            cmds.select(chain[0])
            Interface.orientJoints(self, args)
            cmds.select(deselect=True)

        def constraintJoints(fk, ik, arm):
            for i, j, o in zip(fk, ik, arm):
                cmds.parentConstraint(i, j, o, mo=False, w=1)

        dropdown = cmds.optionMenuGrp('optMenu', query=True, sl=True) - 1

        if dropdown == 0:

            duplicateChain(self.l_ikJoints, self.l_armJoints)
            duplicateChain(self.l_fkJoints, self.l_armJoints)

            mirrorJoints('l_clavicle_jnt')
            mirrorJoints('l_upperArm_FK_jnt')
            mirrorJoints('l_upperArm_IK_jnt')

            constraintJoints(self.l_fkJoints, self.l_ikJoints, self.l_armJoints)
            constraintJoints(self.r_fkJoints, self.r_ikJoints, self.r_armJoints)

    def getPVctrlPosition(self, armPos, elbowPos, wristPos, side):

        armVec = om.MVector(armPos[0], armPos[1], armPos[2])  # Create vector for each joint
        elbowVec = om.MVector(elbowPos[0], elbowPos[1], elbowPos[2])
        wristVec = om.MVector(wristPos[0], wristPos[1], wristPos[2])

        midPoint = (wristVec - armVec) * 0.5 + armVec  # Subtract the arm position from the wrist position, multiply by 0.5 to find the midpoint.
        # + armVec places the new vector at the arm's position
        poleVectorPos = (elbowVec - midPoint) * 10 + elbowVec  # Subtract the midpoint from the elbow's and place it on the elbow
        # (+ elbowVec) to find where the pole vector should be. Multiply brackets result to extend position farther out

        cmds.move(poleVectorPos.x, poleVectorPos.y, poleVectorPos.z, cmds.curve(n=side + 'elbow_ctrl', d=True, p=self.switchCtrlPoints, k=self.switchCtrlPCount))  # Place locator on the calculated position
        cmds.xform(side + 'elbow_ctrl', ro=[0, 0, 90])
        changeShapeColor(side + 'elbow_ctrl', 13)

    @staticmethod
    def setPVctrlPosition(armPos, elbowPos, wristPos, side):

        armVec = om.MVector(armPos[0], armPos[1], armPos[2])
        elbowVec = om.MVector(elbowPos[0], elbowPos[1], elbowPos[2])
        wristVec = om.MVector(wristPos[0], wristPos[1], wristPos[2])

        midPoint = (wristVec - armVec) * 0.5 + armVec
        poleVectorPos = (elbowVec - midPoint) * 1.5 + elbowVec

        cmds.matchTransform(side + 'arm_ikHandle_ctrl', side + 'hand_jnt')
        cmds.move(poleVectorPos.x, poleVectorPos.y, poleVectorPos.z, side + 'elbow_ctrl', rpr=True)

    def createFKcontrols(self, args):

        primaryAxis = cmds.radioButtonGrp(self.radioGroup1, query=True, sl=True)

        left = 'l_'
        right = 'r_'

        def fkControls(side):
            cmds.select(side + 'clavicle_jnt', hi=True)
            cmds.select(side + 'upperArm_FK_jnt', hi=True, add=True)
            jointList = cmds.ls(sl=True, et='joint')

            for i in jointList:
                if 'Nub' in i:
                    jointList.pop(jointList.index(i))

            jointPositions = []
            for i in jointList:
                jointPositions.append(cmds.xform(i, q=1, ws=1, rp=1))

            ctrlList = []
            for i, j in zip(jointList, jointPositions):  # Create controllers, rename and position them on the joints
                cmds.xform(cmds.circle(n=i[:-4] + '_ctrl', r=7), t=j)
                ctrlList.append(i[:-4] + '_ctrl')  # Append controllers names to ctrlList

            for i in ctrlList:
                if 'Finger' in i or 'thumb' in i:  # If the controller is a finger controller, set smaller radius
                    cmds.circle(i, e=True, r=1.5)

            if primaryAxis == 1:
                for i in ctrlList:
                    cmds.circle(i, e=True, nr=[1, 0, 0])  # Set normal orientation for the controllers based on primary axis orientation
                    changeShapeColor(i, 17)
            elif primaryAxis == 2:
                for i in ctrlList:
                    cmds.circle(i, e=True, nr=[0, 1, 0])
                    changeShapeColor(i, 17)
            elif primaryAxis == 3:
                for i in ctrlList:
                    cmds.circle(i, e=True, nr=[0, 0, 1])
                    changeShapeColor(i, 17)

            offsetList = []
            for i, j in zip(ctrlList, jointList):
                offsetList.append(cmds.group(i, name=i[:-4] + 'offset'))  # Group each controller and add the name to a list

            for i, j, o in zip(ctrlList, jointList, offsetList):
                cmds.matchTransform(o, j)
                cmds.makeIdentity(o, apply=True, translate=True)  # Freeze transformations
                cmds.makeIdentity(i, apply=True)  # Freeze transformations
                cmds.delete(i, constructionHistory=True)  # Delete construction history
                cmds.parentConstraint(i, j, maintainOffset=False)  # Constrain joints to controls

            for i, j in zip(ctrlList[:-1], offsetList[:-1]):  #
                offset = offsetList[offsetList.index(j) + 1]
                ctrl = ctrlList[ctrlList.index(i)]
                cmds.parent(offset, ctrl)  # Parent controls under each other

            cmds.parent(side + 'upperArm_offset', world=True)  # unparent controls for the main joint chain
            cmds.parent(side + 'thumb01_offset', world=True)
            cmds.delete(side + 'upperArm_offset')  # Delete main joint chain controls
            cmds.parent(side + 'upperArm_FK_offset', side + 'clavicle_ctrl')  # Parent FK controls to l_clavicle_ctrl

            cmds.select(deselect=True)
            fingersGroup = side + 'fingers_ctrl_offset'
            fingersCtrl = side + 'fingers_ctrl'

            cmds.group(name=fingersGroup, em=True)
            cmds.matchTransform(fingersGroup, side + 'hand_jnt')
            cmds.makeIdentity(fingersGroup, apply=True, translate=True)  # Freeze transformations
            cmds.select(deselect=True)

            fingers = []
            if side is left:
                for i in self.l_fingerLocators:
                    fingers.append(i[0].replace('loc', 'offset'))
            elif side is right:
                for i in self.r_fingerLocators:
                    fingers.append(i[0].replace('loc', 'offset'))

            for i in fingers:
                cmds.parent(i, fingersGroup)  # Parent fingers to new group

            cmds.parentConstraint(side + 'hand_jnt', side + 'fingers_ctrl_offset', mo=False, w=1)

        fkControls(left)
        fkControls(right)

    def createIKcontrols(self, args):

        primaryAxis = cmds.radioButtonGrp(self.radioGroup1, query=True, sl=True)

        left = 'l_'
        right = 'r_'

        def ikControls(side):

            ikName = side + 'arm_ikHandle'
            ikCtrl = side + 'arm_ikHandle_ctrl'

            startJoint = []
            endJoint = []
            if side is left:
                startJoint = self.l_ikJoints[0]
                endJoint = self.l_ikJoints[2]
            elif side is right:
                startJoint = self.r_ikJoints[0]
                endJoint = self.r_ikJoints[2]

            cmds.ikHandle(name=ikName, startJoint=startJoint, endEffector=endJoint, sol='ikRPsolver')  # Create IK handle
            cmds.circle(n=ikCtrl, r=8, nr=self.normal[primaryAxis - 1])   # Create IK controller and position it on the joint

            offsetGroup = cmds.group(name=ikCtrl + '_offset')
            cmds.matchTransform(offsetGroup, side + 'hand_jnt')
            cmds.parent(ikName, ikCtrl)
            cmds.matchTransform(ikCtrl, offsetGroup)
            cmds.orientConstraint(ikCtrl, side + 'hand_IK_jnt')
            changeShapeColor(ikCtrl, 13)
            cmds.makeIdentity(ikName, apply=True)
            cmds.makeIdentity(offsetGroup, apply=True, translate=True)  # Freeze transformations
            cmds.makeIdentity(ikCtrl, apply=True)
            cmds.delete(ikCtrl, constructionHistory=True)

            l_IkFkSwitchPosition = cmds.xform(self.l_ikJoints[2], q=1, ws=1, rp=1)
            l_IkFkSwitchPosition[2] = l_IkFkSwitchPosition[2] - 20
            r_IkFkSwitchPosition = cmds.xform(self.r_ikJoints[2], q=1, ws=1, rp=1)
            r_IkFkSwitchPosition[2] = r_IkFkSwitchPosition[2] - 20

            if side is left:
                cmds.xform(cmds.curve(n=side + 'IK_FK_switch', d=True, p=self.switchCtrlPoints, k=self.switchCtrlPCount), t=l_IkFkSwitchPosition)
                changeShapeColor(side + 'IK_FK_switch', 18)
            if side is right:
                cmds.xform(cmds.curve(n=side + 'IK_FK_switch', d=True, p=self.switchCtrlPoints, k=self.switchCtrlPCount), t=r_IkFkSwitchPosition)
                changeShapeColor(side + 'IK_FK_switch', 18)

            cmds.addAttr(longName=side + 'IK_FK_switch', attributeType='double', min=0, max=1, defaultValue=0)
            cmds.setAttr(side + 'IK_FK_switch' + '.' + side + 'IK_FK_switch', edit=True, keyable=True)
            cmds.makeIdentity(side + 'IK_FK_switch', apply=True)
            cmds.delete(side + 'IK_FK_switch', constructionHistory=True)

            arm_ik_pos = cmds.xform(side + 'upperArm_IK_jnt', q=True, ws=True, t=True)  # Query positions in space of the IK joints and feed them
            elbow_ik_pos = cmds.xform(side + 'foreArm_IK_jnt', q=True, ws=True, t=True)  # to the function, so you can convert them in vectors
            wrist_ik_pos = cmds.xform(side + 'hand_IK_jnt', q=True, ws=True, t=True)

            self.getPVctrlPosition(arm_ik_pos, elbow_ik_pos, wrist_ik_pos, side)

            cmds.makeIdentity(side + 'elbow_ctrl', apply=True)
            cmds.delete(side + 'elbow_ctrl', constructionHistory=True)
            cmds.group(name=side + 'elbow_ctrl' + '_offset')
            cmds.matchTransform(cmds.poleVectorConstraint(side + 'elbow_ctrl', ikName), side + 'hand_IK_jnt')

            cmds.shadingNode('reverse', asUtility=True, name=side + 'IkFkReverse')
            cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', side + 'IkFkReverse.inputX')

            if side is left:
                for i, j, f in zip(self.l_armJoints, self.l_ikJoints, self.l_fkJoints):
                    cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', i + '_parentConstraint1.' + j + 'W1', force=True)
                    cmds.connectAttr(side + 'IkFkReverse.outputX', i + '_parentConstraint1.' + f + 'W0', force=True)
            elif side is right:
                for i, j, f in zip(self.r_armJoints, self.r_ikJoints, self.r_fkJoints):
                    cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', i + '_parentConstraint1.' + j + 'W1', force=True)
                    cmds.connectAttr(side + 'IkFkReverse.outputX', i + '_parentConstraint1.' + f + 'W0', force=True)

            cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', side + 'arm_ikHandle_ctrl_offset.visibility', force=True)
            cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', side + 'elbow_ctrl_offset.visibility', force=True)
            cmds.connectAttr(side + 'IkFkReverse.outputX', side + 'upperArm_FK_offset.visibility', force=True)

        ikControls(left)
        ikControls(right)

    def snapIKFK(self, args):

        left = 'l_'
        right = 'r_'

        nurbs = cmds.ls(et='nurbsCurve')
        selection = cmds.ls(sl=True)

        side = []
        for i in nurbs:
            if selection[0] in i:
                if left in i:
                    side = left
                elif right in i:
                    side = right

        arm_fk_pos = cmds.xform(side + 'upperArm_FK_jnt', q=True, ws=True, t=True)  # Query positions in space of the IK joints and feed them
        elbow_fk_pos = cmds.xform(side + 'foreArm_FK_jnt', q=True, ws=True, t=True)  # to the function, so you can convert them in vectors
        wrist_fk_pos = cmds.xform(side + 'hand_FK_jnt', q=True, ws=True, t=True)

        if cmds.getAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch') == 1:
            cmds.matchTransform(side + 'upperArm_FK_ctrl', side + 'upperArm_jnt')
            cmds.matchTransform(side + 'foreArm_FK_ctrl', side + 'foreArm_jnt')
            cmds.matchTransform(side + 'hand_FK_ctrl', side + 'hand_jnt')
            cmds.setAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', 0)

        elif cmds.getAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch') == 0:
            self.setPVctrlPosition(arm_fk_pos, elbow_fk_pos, wrist_fk_pos, side)
            cmds.setAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', 1)

    def setXYZp(self, args):                                        # Radio buttons logic
        a = cmds.radioButtonGrp(self.radioGroup1, q=True, sl=True)
        b = cmds.radioButtonGrp(self.radioGroup2, q=True, sl=True)
        if a == 1 and b == 1:
            cmds.radioButtonGrp(self.radioGroup2, e=True, sl=2)
        elif a == 2 and b == 2:
            cmds.radioButtonGrp(self.radioGroup2, e=True, sl=3)
        elif a == 3 and b == 3:
            cmds.radioButtonGrp(self.radioGroup2, e=True, sl=1)

    def setXYZs(self, args):
        a = cmds.radioButtonGrp(self.radioGroup1, q=True, sl=True)
        b = cmds.radioButtonGrp(self.radioGroup2, q=True, sl=True)
        if b == 1 and a == 1:
            cmds.radioButtonGrp(self.radioGroup1, e=True, sl=2)
        elif b == 2 and a == 2:
            cmds.radioButtonGrp(self.radioGroup1, e=True, sl=3)
        elif b == 3 and a == 3:
            cmds.radioButtonGrp(self.radioGroup1, e=True, sl=1)

    def checkboxState(self, args):
        if cmds.checkBox(self.checkbox1, q=True, v=True) == 1:
            cmds.columnLayout(self.layout2, e=True, en=0)
        elif cmds.checkBox(self.checkbox1, q=True, v=True) == 0:
            cmds.columnLayout(self.layout2, e=True, en=1)

    def noneChecked(self, args):
        cmds.radioButtonGrp(self.radioGroup3, e=True, en=0)

    def noneUnchecked(self, args):
        cmds.radioButtonGrp(self.radioGroup3, e=True, en=1)


newWindow = Interface()
