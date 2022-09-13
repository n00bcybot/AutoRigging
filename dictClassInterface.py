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
def alignTransAxis(args):  # Aligning translation axis', in case they have been rotated, for the thumb for example
    x = cmds.ls(sl=True)
    for i in x:
        cmds.joint(i, edit=True, zso=True)


# noinspection PyUnusedLocal
def parentFingers():
    y = []  # Parent all fingers to hand joint
    for each in Interface.l_fingerLocators:
        y.append(each[0].replace('_loc', '_jnt'))
    for i in y:
        cmds.parent(i, 'l_hand_jnt')
        cmds.select(deselect=True)


# noinspection PyUnusedLocal
def unparentFingers():
    y = []
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

    ctrlList = [side + 'upperArm_FK_ctrl', side + 'foreArm_FK_ctrl', side + 'hand_FK_ctrl', side + 'arm_ikHandle_ctrl',
                side + 'elbow_ctrl']
    xyz = ['X', 'Y', 'Z']
    for i in ctrlList:
        for j in xyz:
            cmds.setAttr(i + '.rotate' + j, 0)
            cmds.setAttr(i + '.translate' + j, 0)


# noinspection PyUnusedLocal
def mirrorJoints(joint):

    if joint == 'l_eye_jnt':
        cmds.mirrorJoint(joint, mirrorYZ=True, searchReplace=('l_', 'r_'))
    else:
        cmds.mirrorJoint(joint, mirrorYZ=True, mirrorBehavior=True, searchReplace=('l_', 'r_'))


# noinspection PyUnusedLocal
def getJointWP(jnt):
    cmds.spaceLocator()
    locator = cmds.ls(sl=True)[0]
    jointList = cmds.ls(et='joint')
    if jnt not in jointList:
        pointWP = cmds.xform(jnt, q=True, t=True)
    else:
        cmds.matchTransform(locator, jnt)
        pointWP = cmds.xform(locator, q=True, t=True)
    cmds.delete(locator)
    return pointWP


# noinspection PyUnusedLocal
def movePivot(obj, jointName):

    world = [0, 0, 0]

    if jointName == 'world':
        point = world
    else:
        point = getJointWP(jointName)

    if jointName == 'l_toeNub_jnt' or jointName == 'r_toeNub_jnt':
        x = point[0]
        y = 0
        z = point[2]
    else:
        x = point[0]
        y = point[1]
        z = point[2]

    cmds.move(x, y, z, obj + '.scalePivot', obj + '.rotatePivot')


# noinspection PyUnusedLocal
def getPrimaryAxis(jnt):

    cmds.select(jnt, hi=True)
    jointList = cmds.ls(sl=True)

    joint2pos = cmds.joint(jointList[1], q=True, r=True)

    x = abs(joint2pos[0])
    y = abs(joint2pos[1])
    z = abs(joint2pos[2])

    xyz = [x, y, z]

    for i in xyz:
        if i == max(xyz):
            return xyz.index(i) + 1


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
        'pelvis_loc': [0, 97, 0],
        'root_loc': [0.0, 0.0, 0.0],
        'spine_01_loc': [1.2988677644386279e-06, 107.55629733472321, -0.1652469392414555],
        'spine_02_loc': [3.547265996651281e-06, 126.76314604454366, -1.51601391020198],
        'spine_03_loc': [5.141275897605e-06, 140.029842391107, -3.497939646387775]
    }

    locTemp = {

        'root_loc': [0.0, 0.0, 0.0],
        'pelvis_loc': [0.0, 105, 0],
        'spine01_loc': [0.0, 120, 1],
        'spine02_loc': [0.0, 135, -2],
        'neck01_loc': [0, 151, 1],
        'neck02_loc': [0, 155, 0],
        'head_loc': [0, 164, 1],

        'jawNub_loc': [0, 158, 8.5],
        'jaw_loc': [0, 161, 2.5],

        'l_eyeNub_loc': [2.8762510108536112, 169.08230670451212, 8.743195847205346],
        'l_eye_loc': [2.8762517261093254, 169.08230670451212, 7.192147091559658],

        'l_clavicle_loc': [4, 148.14189486770232, 4.467180828980827],
        'l_upperArm_loc': [13, 148, 0],
        'l_foreArm_loc': [38.48, 148.655, -1.872],
        'l_hand_loc': [63.927, 148.655, 0],
        'l_thumb01_loc': [69.519, 146.426, 3.435],
        'l_thumb02_loc': [71.885, 145.75, 4.146],
        'l_thumbNub_loc': [73.868, 145.051, 4.462],
        'l_indexFinger01_loc': [71.793, 148.43, 2.434],
        'l_indexFinger02_loc': [74.447, 148.286, 2.864],
        'l_indexFinger03_loc': [76.73, 147.484, 3.234],
        'l_indexFingerNub_loc': [78.326, 146.08, 3.498],
        'l_middleFinger01_loc': [72.723, 148.866, 0.542],
        'l_middleFinger02_loc': [75.335, 148.654, 0.733],
        'l_middleFinger03_loc': [77.73, 147.892, 0.902],
        'l_middleFingerNub_loc': [79.748, 146.256, 1.054],
        'l_ringFinger01_loc': [72.31, 148.749, -1.171],
        'l_ringFinger02_loc': [74.771, 148.55, -1.323],
        'l_ringFinger03_loc': [76.794, 147.946, -1.464],
        'l_ringFingerNub_loc': [78.711, 146.434, -1.579],
        'l_pinkyFinger01_loc': [72.09, 148.599, -2.88],
        'l_pinkyFinger02_loc': [73.67, 148.437, -3.116],
        'l_pinkyFinger03_loc': [75.537, 147.957, -3.414],
        'l_pinkyFingerNub_loc': [77.032, 147.083, -3.638],

        'l_thigh_loc': [9.016487120738676, 103.21524918079396, -0.06317702051060863],
        'l_calf_loc': [9.016487172208775, 55.99999943954483, 4.0000000438007675],
        'l_ankle_loc': [9.01648766284925, 8.999999803973829, -3.0000015635754016],
        'l_toeNub_loc': [9.016487800761242, 1.0000001203622366, 15.9999991785903],
        'l_toe_loc': [9.016487734626331, 1.0000008199679824, 4.999999178590323],

        #  'COMOffset_loc': [0.0, 105.0, 0.0],
        #  'COM_loc': [0.0, 105, 0.0],
        #  'head01_loc': [-2.6069044344454757e-07, 155, -2],
        #  'head02_loc': [-3.94965337055097e-07, 164, -1],
        #  'headNub_loc': [-1.7498294615581403e-15, 178.64732454094343, -7.2398515053674455],
        #  'neck02_loc': [-2.1416909327475675e-07, 159.46418229884728, -1.8036069109735917],
        #  'spine02_loc': [0.0, 118, 1],
        #  'spine03_loc': [0.0, 135, -3],
        #  'spine04_loc': [0.0, 148.43186463177227, -3.0205814470408088]
    }

    ### L locators

    l_thumbLocators = ['l_thumb01_loc', 'l_thumb02_loc', 'l_thumbNub_loc']
    l_indexLocators = ['l_indexFinger01_loc', 'l_indexFinger02_loc', 'l_indexFinger03_loc', 'l_indexFingerNub_loc']
    l_middleLocators = ['l_middleFinger01_loc', 'l_middleFinger02_loc', 'l_middleFinger03_loc', 'l_middleFingerNub_loc']
    l_ringLocators = ['l_ringFinger01_loc', 'l_ringFinger02_loc', 'l_ringFinger03_loc', 'l_ringFingerNub_loc']
    l_pinkyLocators = ['l_pinkyFinger01_loc', 'l_pinkyFinger02_loc', 'l_pinkyFinger03_loc', 'l_pinkyFingerNub_loc']
    l_armLocators = ['l_clavicle_loc', 'l_upperArm_loc', 'l_foreArm_loc', 'l_hand_loc']
    spineLocators = ['pelvis_loc', 'spine01_loc', 'spine02_loc', 'neck01_loc', 'neck02_loc', 'head_loc']
    l_legLocators = ['l_thigh_loc', 'l_calf_loc', 'l_ankle_loc', 'l_toe_loc', 'l_toeNub_loc']
    l_eyeLocators = ['l_eye_loc', 'l_eyeNub_loc']
    jawLocators = ['jaw_loc', 'jawNub_loc']

    l_arm_ikJoints = ['l_upperArm_IK_jnt', 'l_foreArm_IK_jnt', 'l_hand_IK_jnt']
    l_arm_fkJoints = ['l_upperArm_FK_jnt', 'l_foreArm_FK_jnt', 'l_hand_FK_jnt']
    l_arm_joints = ['l_upperArm_jnt', 'l_foreArm_jnt', 'l_hand_jnt']

    l_leg_ikJoints = ['l_thigh_IK_jnt', 'l_calf_IK_jnt', 'l_ankle_IK_jnt']
    l_leg_joints = ['l_thigh_jnt', 'l_calf_jnt', 'l_ankle_jnt']

    ### R locators

    r_thumbLocators = ['r_thumb01_loc', 'r_thumb02_loc', 'r_thumbNub_loc']
    r_indexLocators = ['r_indexFinger01_loc', 'r_indexFinger02_loc', 'r_indexFinger03_loc', 'r_indexFingerNub_loc']
    r_middleLocators = ['r_middleFinger01_loc', 'r_middleFinger02_loc', 'r_middleFinger03_loc', 'r_middleFingerNub_loc']
    r_ringLocators = ['r_ringFinger01_loc', 'r_ringFinger02_loc', 'r_ringFinger03_loc', 'r_ringFingerNub_loc']
    r_pinkyLocators = ['r_pinkyFinger01_loc', 'r_pinkyFinger02_loc', 'r_pinkyFinger03_loc', 'r_pinkyFingerNub_loc']

    r_fingerLocators = [r_thumbLocators, r_indexLocators, r_middleLocators, r_ringLocators, r_pinkyLocators]

    r_arm_ikJoints = ['r_upperArm_IK_jnt', 'r_foreArm_IK_jnt', 'r_hand_IK_jnt']
    r_arm_fkJoints = ['r_upperArm_FK_jnt', 'r_foreArm_FK_jnt', 'r_hand_FK_jnt']
    r_arm_joints = ['r_upperArm_jnt', 'r_foreArm_jnt', 'r_hand_jnt']

    r_leg_ikJoints = ['r_thigh_IK_jnt', 'r_calf_IK_jnt', 'r_ankle_IK_jnt']
    r_leg_joints = ['r_thigh_jnt', 'r_calf_jnt', 'r_ankle_jnt']

    ### Global locators

    l_fingerLocators = [l_thumbLocators, l_indexLocators, l_middleLocators, l_ringLocators, l_pinkyLocators]
    l_handLocators = [l_armLocators, l_thumbLocators, l_indexLocators, l_middleLocators, l_ringLocators,
                      l_pinkyLocators]

    allLists = [l_armLocators, l_legLocators, spineLocators, l_eyeLocators, jawLocators, l_thumbLocators,
                l_indexLocators, l_middleLocators, l_ringLocators, l_pinkyLocators]
    allChains = [l_handLocators, l_legLocators, spineLocators, l_eyeLocators, jawLocators, allLists]

    ### Switches and controls

    IKFK_switchCtrlPoints = [(0, 0, 0), (2, 0, -2), (2, 0, -1), (6, 0, -1), (6, 0, -2), (8, 0, 0), (6, 0, 2), (6, 0, 1),
                             (2, 0, 1), (2, 0, 2), (0, 0, 0)]
    IKFK_switchCtrlPCount = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    spine_Ctrl_Points = [(0.0, 0.0, 0.0), (200.0, 0.0, -200.0), (200.0, 0.0, -100.0),
                         (300.0, 0.0, -100.0), (500.0, 0.0, -300.0), (500.0, 0.0, -400.0),
                         (400.0, 0.0, -400.0), (600.0, 0.0, -600.0), (800.0, 0.0, -400.0),
                         (700.0, 0.0, -400.0), (700.0, 0.0, -300.0), (900.0, 0.0, -100.0),
                         (1000.0, 0.0, -100.0), (1000.0, 0.0, -200.0), (1200.0, 0.0, 0.0),
                         (1000.0, 0.0, 200.0), (1000.0, 0.0, 100.0), (900.0, 0.0, 100.0),
                         (700.0, 0.0, 300.0), (700.0, 0.0, 400.0), (800.0, 0.0, 400.0),
                         (600.0, 0.0, 600.0), (400.0, 0.0, 400.0), (500.0, 0.0, 400.0),
                         (500.0, 0.0, 300.0), (300.0, 0.0, 100.0), (200.0, 0.0, 100.0),
                         (200.0, 0.0, 200.0), (0.0, 0.0, 0.0)]
    spine_Ctrl_PCount = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                         26, 27, 28]
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
        cmds.menuItem(label='Arms')
        cmds.menuItem(label='Legs')
        cmds.menuItem(label='Spine')
        cmds.menuItem(label='Eyes')
        cmds.menuItem(label='Jaw')
        cmds.menuItem(label='All chains')

        self.layout1 = cmds.columnLayout(adjustableColumn=True, ebg=True, parent=self.tab1)
        self.layout3 = cmds.columnLayout(parent=self.layout1, cw=470, cat=('both', 142))

        self.checkbox1 = cmds.checkBox(label='Orient Joint To World', value=0, onc=self.checkboxState,
                                       ofc=self.checkboxState, parent=self.layout3)
        self.layout2 = cmds.columnLayout(adjustableColumn=True, ebg=True, parent=self.layout1)
        self.radioGroup1 = cmds.radioButtonGrp(nrb=3, label='Primary Axis', labelArray3=['X', 'Y', 'Z'],
                                               cw=([2, 70], [3, 70]), sl=1, p=self.layout2, on1=self.setXYZp,
                                               on2=self.setXYZp, on3=self.setXYZp)
        self.radioGroup2 = cmds.radioButtonGrp(nrb=4, label='Secondary Axis', labelArray4=['X', 'Y', 'Z', 'None'],
                                               cw=([2, 70], [3, 70], [4, 70]), sl=2, p=self.layout2, on1=self.setXYZs,
                                               on2=self.setXYZs, on3=self.setXYZs, on4=self.noneChecked,
                                               of4=self.noneUnchecked)
        self.radioGroup3 = cmds.radioButtonGrp(nrb=3, label='SA World Orientation', labelArray3=['X', 'Y', 'Z'],
                                               cw=([2, 70], [3, 70], [4, 70]), sl=2, p=self.layout2)

        self.slider1 = cmds.intSliderGrp('slider1', label='Orientation Tolerance', field=True, value=90, height=20, max=180, p=self.layout2)
        self.thumbLayout = cmds.rowColumnLayout('thumbLayout', numberOfColumns=1, adj=True, parent=self.layout2)
        self.slider2 = cmds.intSliderGrp('slider2', label='Thumb Rotation', field=True, value=-50, height=20, min=-180, max=180, p=self.thumbLayout)

        cmds.optionMenuGrp('updown', parent=self.radioGroup3)
        cmds.menuItem(label='+')
        cmds.menuItem(label='-')

        cmds.button(label='Spawn Locators', p=self.tab1, command=self.spawnTempLocators, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Spawn Joints', p=self.tab1, command=self.createJointChain, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Orient Joints', p=self.tab1, command=self.orientJoints, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Duplicate Joints', p=self.tab1, command=self.duplicateJoints, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Create FK Controls', p=self.tab1, command=self.createFKcontrols, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Create IK Controls', p=self.tab1, command=self.createIKcontrols, height=30)

        cmds.separator(height=2, st='none')
        cmds.button(label='Snap FK to IK / IK to FK', p=self.tab1, command=self.snapIKFK, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Connect Components', p=self.tab1, command=self.connectComponents, height=30)

        self.tab2 = cmds.columnLayout(adjustableColumn=True, ebg=True, parent=self.tabs)
        cmds.separator(height=2, st='none')
        cmds.button(label='Select Hierarchy', command=selectHierarchy, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Display/Hide Local Orientation Axis', command=displayLocalAxis, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Match Transformations', command=matchAllTransform, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Select All Joints', command=selectAllJoints, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Delete All Locators', command=deleteAllLocators, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Disable/Enable Scale Compensation', command=disableScaleComp, height=30)
        cmds.separator(height=2, st='none')
        cmds.button(label='Reset Controls', p=self.tab2, command=resetControls, height=30)
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
        cmds.select(d=True)

    @staticmethod
    def spawnJoints(slist):  # Create joints from list

        x = cmds.ls(type='locator', s=False)  # Create dictionary from locators in the scene,  with locators'
        y = [i.replace('Shape', '') for i in x]

        locatorsPositions = []  # names as keys and their positions in space, as values.
        for i in y:  # Joints will be spawned from this dictionary
            locatorsPositions.append(cmds.pointPosition(i, world=True))

        newList = []
        newPositions = []
        for i in slist:  # For each item in slist, if the item is in list_B
            if i in y:  # add it to the dictNew
                newList.append(i)  # dictNew[item] becomes the key, = , dictOld[i] gets the corresponding values
                newPositions.append(locatorsPositions[y.index(i)])

        for i, j in zip(newList, newPositions):  # Creating the chain by iterating over the keys and the values
            cmds.joint(n=i.replace('_loc', '_jnt'), position=j)  # in the dictionary

        cmds.select(deselect=True)  # to select the first joint from the list, after the joints are created.

        for i in slist:
            cmds.delete(i)

    def orientJoints(self, args):

        def getDirection(jointChain):

            joint1 = jointChain[0]
            joint2 = jointChain[1]

            number = []
            for i, j in zip(getJointWP(joint2), getJointWP(joint1)):
                number.append(abs(i - j))

            for i in number:
                if i == max(number):
                    if number.index(i) == 0:
                        return 1
                    elif number.index(i) == 1:
                        return 2
                    elif number.index(i) == 2:
                        return 3

        def findNub():  # This function checks whether the joint that needs to be orientated is at the end of the chain, as in, it has no children
            # If it has no children, it will be oriented to the world (meaning it will inherit orientation from the parent joint)

            if cmds.checkBox(self.checkbox1, q=True, v=True) == 1:
                for each in orient:  # thus automatically aligning correctly
                    cmds.joint(each, e=True, oj='none', ch=True, zso=True)
            else:
                if r2 == 4:
                    if r1 == 1:
                        for i in orient:
                            cmds.joint(i, e=True, oj='xyz', ch=True, zso=True)
                    elif r1 == 2:
                        for i in orient:
                            cmds.joint(i, e=True, oj='yzx', ch=True, zso=True)
                    elif r1 == 3:
                        for i in orient:
                            cmds.joint(i, e=True, oj='zxy', ch=True, zso=True)
                else:
                    for each in orient:
                        if cmds.listRelatives(each) is None:
                            cmds.joint(each, e=True, oj='none', ch=True, zso=True)
                        else:
                            cmds.joint(each, e=True, oj=allAxis, sao=secAxis, ch=True, zso=True)
                if 'l_hand_jnt' in orient:
                    self.rotateLocalRotAxis(args=True)

        xyz = ['xyz', 'xzy', 'yxz', 'yzx', 'zxy',
               'zyx']  # List with all possible combinations for primary axis orientation
        a = ['x', 'y', 'z']
        b = ['up', 'down']

        r1 = cmds.radioButtonGrp(self.radioGroup1, query=True, sl=True)
        r2 = cmds.radioButtonGrp(self.radioGroup2, query=True, sl=True)
        r3 = cmds.radioButtonGrp(self.radioGroup3, query=True, sl=True)
        r4 = cmds.optionMenuGrp('updown', query=True, sl=True)

        sel = a[r1 - 1] + a[r2 - 1]  # Querying the radio buttons and setting the desired axis from list 'a'
        allAxis = ''  # The radio buttons produce integers that correspond to the letters of each radio button
        for i in xyz:  # The corresponding letters are then taken from list 'a', concatenated and compared against
            if sel in i[:2]:  # list 'xyz'. The matching string is assigned to 'allAxis', which defines the orientation
                allAxis = i  # of the primary axis

        secAxis = a[r3 - 1] + b[r4 - 1]  # Querying r3 and b to establish orientation for the secondary axis

        cmds.select(hi=True)  # Selecting all joints in the hierarchy
        orient = cmds.ls(sl=True)  # and storing their names in here
        direction = getDirection(orient)
        findNub()
        if 'l_hand_jnt' in orient:  # Checking if 'l_hand_jnt' is in the list of joints, if so, the fingers need to be unparented
            unparentFingers()  # and then orientated. If they are not, the wrist will be oriented towards the next joint

        c = []  # that is created (the thumb), which is wrong in the case of the hand. Rather, it needs to
        y = []
        for each in orient:  # be aligned with the elbow (the world) - that can only happen if it has no children.
            c.append(cmds.joint(each, q=True, o=True))  # Creating the joints and a list with their orientations
        for i in c:  # if any of the xyz orientations equals 180, it means the joint has flipped
            for j in i:  # the following code corrects that with setting the appropriate secondary axis orientation
                y.append(round(abs(j)))

        degrees = cmds.intSliderGrp('slider1', q=True, value=True)

        for i in y:
            if round(i) > degrees:
                if r3 == direction:
                    if direction == 1:
                        secAxis = a[r3 - 2] + b[r4 - 1]
                    elif direction == 2:
                        secAxis = a[r3] + b[r4 - 1]
                    elif direction == 3:
                        secAxis = a[r3 - 3] + b[r4 - 1]

        findNub()
        if 'l_hand_jnt' in orient:
            parentFingers()  # Parents the fingers back

        cmds.select(d=True)

    def rotateLocalRotAxis(self, args):

        x = 0
        y = 0
        z = 0

        sel = cmds.radioButtonGrp(self.radioGroup1, query=True, sl=True) - 1
        sliderQuery = cmds.intSliderGrp('slider2', q=True, value=True)
        if sel == 0:
            x = sliderQuery
        elif sel == 1:
            y = sliderQuery
        elif sel == 2:
            z = sliderQuery
        print(sel)
        cmds.select('l_thumb01_jnt', r=True)
        cmds.hilite('l_thumb01_jnt')
        cmds.select('l_thumb01_jnt.rotateAxis')
        cmds.select('l_thumb02_jnt.rotateAxis', tgl=True)
        cmds.select('l_thumbNub_jnt.rotateAxis', tgl=True)
        cmds.rotate(x, y, z, r=True, os=True, fo=True)
        alignTransAxis(args=True)
        cmds.hilite('l_thumb01_jnt', u=True)

    def createJointChain(self, args):

        selected = cmds.optionMenuGrp('optMenu', query=True, sl=True) - 1  # Querying the dropdown menu
        dropdownList = self.allChains[int(selected)]  # Getting the respective list form allChains

        if isinstance(dropdownList[0], list):  # If selected list contains list (like handLoc)
            for i in dropdownList:  # execute for each sublist
                self.spawnJoints(i)
            parentFingers()
        else:  # else execute list
            self.spawnJoints(dropdownList)

        if isinstance(dropdownList[0],
                      list):  # This part selects the first joint in the hierarchy, so it can orientate it with the function further down
            cmds.select(dropdownList[0][0].replace('_loc', '_jnt'))
        else:
            cmds.select(dropdownList[0].replace('_loc', '_jnt'))

        if selected == 3:
            cmds.select(hi=True)  # Selecting all joints in the hierarchy
            eyeJoints = cmds.ls(sl=True)
            for i in eyeJoints:
                cmds.joint(i, e=True, oj='none', ch=True, zso=True)
        else:
            Interface.orientJoints(self, args=True)

    def duplicateJoints(self, args):

        def duplicateChain(chain, limbs):

            def jointPosition():
                jointPositions = []
                for each in limbs:
                    jointPositions.append(cmds.xform(each, q=1, ws=1, rp=1))
                return jointPositions

            for i, j in zip(chain, jointPosition()):
                cmds.joint(n=i, position=j)
            cmds.select(chain[0])
            Interface.orientJoints(self, args)
            cmds.select(deselect=True)

        def constraintArmJoints(fk, ik, arm):
            for i, j, o in zip(fk, ik, arm):
                cmds.parentConstraint(i, j, o, mo=True, w=1)

        def constraintLegJoints(ik, leg):
            for i, j in zip(ik, leg):
                cmds.parentConstraint(i, j, mo=True, w=1)

        dropdown = cmds.optionMenuGrp('optMenu', query=True, sl=True) - 1

        if dropdown == 0:

            duplicateChain(self.l_arm_ikJoints, self.l_arm_joints)
            duplicateChain(self.l_arm_fkJoints, self.l_arm_joints)

            mirrorJoints('l_clavicle_jnt')
            mirrorJoints('l_upperArm_FK_jnt')
            mirrorJoints('l_upperArm_IK_jnt')

            constraintArmJoints(self.l_arm_fkJoints, self.l_arm_ikJoints, self.l_arm_joints)
            constraintArmJoints(self.r_arm_fkJoints, self.r_arm_ikJoints, self.r_arm_joints)

        elif dropdown == 1:

            duplicateChain(self.l_leg_ikJoints, self.l_leg_joints)

            cmds.matchTransform('l_ankle_IK_jnt', 'l_ankle_jnt')

            mirrorJoints('l_thigh_jnt')
            mirrorJoints('l_thigh_IK_jnt')

            constraintLegJoints(self.l_leg_ikJoints, self.l_leg_joints)
            constraintLegJoints(self.r_leg_ikJoints, self.r_leg_joints)
            cmds.select(d=True)

        elif dropdown == 3:

            mirrorJoints('l_eye_jnt')

    def getPVctrlPosition(self, armPos, elbowPos, wristPos, side):

        armVec = om.MVector(armPos[0], armPos[1], armPos[2])  # Create vector for each joint
        elbowVec = om.MVector(elbowPos[0], elbowPos[1], elbowPos[2])
        wristVec = om.MVector(wristPos[0], wristPos[1], wristPos[2])

        midPoint = (
                               wristVec - armVec) * 0.5 + armVec  # Subtract the arm position from the wrist position, multiply by 0.5 to find the midpoint.
        # + armVec places the new vector at the arm's position
        poleVectorPos = (
                                    elbowVec - midPoint) * 10 + elbowVec  # Subtract the midpoint from the elbow's and place it on the elbow
        # (+ elbowVec) to find where the pole vector should be. Multiply brackets result to extend position farther out

        cmds.move(poleVectorPos.x, poleVectorPos.y, poleVectorPos.z,
                  cmds.curve(n=side + 'elbow_ctrl', d=True, p=self.IKFK_switchCtrlPoints,
                             k=self.IKFK_switchCtrlPCount))  # Place locator on the calculated position
        cmds.xform(side + 'elbow_ctrl', ro=[0, 0, 90])
        changeShapeColor(side + 'elbow_ctrl', 13)

    def getPVkneeCtrlPosition(self, thighPos, kneePos, anklePos, side):

        thighVec = om.MVector(thighPos[0], thighPos[1], thighPos[2])  # Create vector for each joint
        kneeVec = om.MVector(kneePos[0], kneePos[1], kneePos[2])
        ankleVec = om.MVector(anklePos[0], anklePos[1], anklePos[2])

        midPoint = (
                               ankleVec - thighVec) * 0.5 + thighVec  # Subtract the arm position from the wrist position, multiply by 0.5 to find the midpoint.
        # + armVec places the new vector at the arm's position
        poleVectorPos = (
                                    kneeVec - midPoint) * 5 + kneeVec  # Subtract the midpoint from the elbow's and place it on the elbow
        # (+ elbowVec) to find where the pole vector should be. Multiply brackets result to extend position farther out

        cmds.move(poleVectorPos.x, poleVectorPos.y, poleVectorPos.z,
                  cmds.curve(n=side + 'knee_ctrl', d=True, p=self.IKFK_switchCtrlPoints,
                             k=self.IKFK_switchCtrlPCount))  # Place locator on the calculated position
        cmds.xform(side + 'knee_ctrl', ro=[0, 0, 90])
        changeShapeColor(side + 'knee_ctrl', 13)

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

        def armsFKControls(side):

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

            axis = getPrimaryAxis(jointList[1])

            if axis == 1:
                for i in ctrlList:
                    cmds.circle(i, e=True, nr=[1, 0, 0])  # Set normal orientation for the controllers based on primary axis orientation
                    changeShapeColor(i, 17)
            elif axis == 2:
                for i in ctrlList:
                    cmds.circle(i, e=True, nr=[0, 1, 0])
                    changeShapeColor(i, 17)
            elif axis == 3:
                for i in ctrlList:
                    cmds.circle(i, e=True, nr=[0, 0, 1])
                    changeShapeColor(i, 17)

            offsetList = []
            for i, j in zip(ctrlList, jointList):
                offsetList.append(
                    cmds.group(i, name=i[:-4] + 'offset'))  # Group each controller and add the name to a list

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

        def spineFKControls():

            cmds.select('pelvis_jnt', hi=True)
            jointList = cmds.ls(sl=True, et='joint')

            jointPositions = []
            for i in jointList:
                jointPositions.append(cmds.xform(i, q=1, ws=1, rp=1))

            ctrlList = []
            for i, j in zip(jointList, jointPositions):  # Create controllers, rename and position them on the joints
                cmds.xform(cmds.circle(n=i[:-4] + '_ctrl', r=18), t=j)
                ctrlList.append(i[:-4] + '_ctrl')  # Append controllers names to ctrlList

            axis = getPrimaryAxis(jointList[1])
            if axis == 1:
                for i in ctrlList:
                    cmds.circle(i, e=True, nr=[1, 0, 0])  # Set normal orientation for the controllers based on primary axis orientation
                    changeShapeColor(i, 14)
            elif axis == 2:
                for i in ctrlList:
                    cmds.circle(i, e=True, nr=[0, 1, 0])
                    changeShapeColor(i, 14)
            elif axis == 3:
                for i in ctrlList:
                    cmds.circle(i, e=True, nr=[0, 0, 1])
                    changeShapeColor(i, 14)

            offsetList = []
            for i, j in zip(ctrlList, jointList):
                offsetList.append(
                    cmds.group(i, name=i[:-4] + 'offset'))  # Group each controller and add the name to a list

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

            spineController = 'spine_ctrl'  # Create spine control
            cmds.xform(cmds.curve(name=spineController, d=True, p=self.spine_Ctrl_Points, k=self.spine_Ctrl_PCount),
                       t=self.locTemp['spine01_loc'], cp=True)

            cmds.matchTransform(spineController, 'pelvis_jnt', px=True, pz=True, pos=True)
            cmds.scale(0.07, 0.07, 0.07, spineController, absolute=True)
            changeShapeColor(spineController, 18)
            cmds.group(spineController, name=spineController + '_offset')
            cmds.makeIdentity(spineController, apply=True)
            cmds.delete(spineController, constructionHistory=True)

            waistController = 'waist_ctrl'
            cmds.circle(n=waistController, r=20, nr=self.normal[1])
            cmds.matchTransform(waistController, 'pelvis_jnt', px=True, pz=True, pos=True)
            changeShapeColor(waistController, 14)
            pelvisPosition = getJointWP('pelvis_jnt')
            cmds.move(round(pelvisPosition[1] - 10), waistController, y=True)
            cmds.group(waistController, name=waistController + '_offset')
            cmds.makeIdentity(waistController, apply=True)
            cmds.delete(waistController, constructionHistory=True)
            movePivot('waist_ctrl', 'spine01_jnt')
            cmds.parent('pelvis_offset', 'spine_ctrl')
            cmds.parent('waist_ctrl_offset', 'spine_ctrl')
            cmds.delete('pelvis_jnt_parentConstraint1')
            cmds.parentConstraint('waist_ctrl', 'pelvis_jnt', maintainOffset=True)

        def eyesFKcontrols(side):

            eye = side + 'eye_jnt'
            jointPosition = cmds.xform(eye, q=1, ws=1, rp=1)

            eye_ctrl = eye[:-4] + '_ctrl'
            cmds.xform(cmds.circle(name=eye_ctrl, r=2), t=jointPosition)
            cmds.circle(side + 'eye_ctrl', e=True, nr=[0, 0, 1])
            changeShapeColor(eye_ctrl, 23)
            offsetGrp = cmds.group(name=eye[:-4] + '_offset')
            cmds.matchTransform(offsetGrp, eye)
            cmds.move((jointPosition[2] + 30), eye_ctrl, z=True)
            cmds.makeIdentity(offsetGrp, apply=True, translate=True)  # Freeze transformations
            cmds.makeIdentity(eye_ctrl, apply=True)  # Freeze transformations
            cmds.delete(eye_ctrl, constructionHistory=True)  # Delete construction history

        def jawFKcontrols():

            jaw = 'jaw_jnt'
            jointPosition = cmds.xform(jaw, q=1, ws=1, rp=1)
            jaw_ctrl = jaw[:-4] + '_ctrl'
            cmds.xform(cmds.circle(name=jaw_ctrl, r=7), t=jointPosition)
            cmds.circle(jaw_ctrl, e=True, nr=[1, 0, 0])
            changeShapeColor(jaw_ctrl, 12)
            cmds.matchTransform(jaw_ctrl, jaw)
            offsetGrp = cmds.group(name=jaw[:-4] + '_offset', em=True)
            cmds.matchTransform(offsetGrp, jaw)
            cmds.makeIdentity(offsetGrp, apply=True, translate=True)
            cmds.parent(jaw_ctrl, offsetGrp)
            cmds.makeIdentity(jaw_ctrl, apply=True)

            cmds.parentConstraint(jaw_ctrl, jaw)

        dropdown = cmds.optionMenuGrp('optMenu', query=True, sl=True) - 1

        if dropdown == 2:
            spineFKControls()

        elif dropdown == 0:
            armsFKControls(left)
            armsFKControls(right)

        elif dropdown == 3:

            eyesFKcontrols('l_')
            eyesFKcontrols('r_')

            eyeCtrl = 'eye_ctrl'
            midPosition = (getJointWP('r_eye_jnt')[0] - getJointWP('l_eye_jnt')[0]) / 2 + getJointWP('l_eye_jnt')[0]
            lEyePos = cmds.xform('l_eye_jnt', q=1, ws=1, rp=1)
            cmds.xform(cmds.circle(name=eyeCtrl, r=6), t=lEyePos)
            cmds.circle(eyeCtrl, e=True, nr=[0, 0, 1])
            changeShapeColor(eyeCtrl, 23)
            cmds.move((lEyePos[2] + 30), eyeCtrl, z=True)
            cmds.move(midPosition, eyeCtrl, x=True)
            cmds.makeIdentity(eyeCtrl, apply=True)
            cmds.delete(eyeCtrl, constructionHistory=True)

            cmds.group(em=True, name='eye_ctrl_offset')
            cmds.parent(eyeCtrl, 'eye_ctrl_offset')
            cmds.parent('l_eye_offset', eyeCtrl)
            cmds.parent('r_eye_offset', eyeCtrl)
            cmds.aimConstraint('l_eye_ctrl', 'l_eye_jnt', mo=True)
            cmds.aimConstraint('r_eye_ctrl', 'r_eye_jnt', mo=True)
            cmds.xform('eye_ctrl_offset', cp=True)
            cmds.makeIdentity('eye_ctrl_offset', apply=True)

        elif dropdown == 4:

            jawFKcontrols()

    def createIKcontrols(self, args):

        primaryAxis = cmds.radioButtonGrp(self.radioGroup1, query=True, sl=True)

        left = 'l_'
        right = 'r_'

        def arm_ikControls(side):

            ikName = side + 'arm_ikHandle'
            ikCtrl = side + 'arm_ikHandle_ctrl'

            startJoint = []
            endJoint = []
            if side is left:
                startJoint = self.l_arm_ikJoints[0]
                endJoint = self.l_arm_ikJoints[2]
            elif side is right:
                startJoint = self.r_arm_ikJoints[0]
                endJoint = self.r_arm_ikJoints[2]

            cmds.ikHandle(name=ikName, startJoint=startJoint, endEffector=endJoint,
                          sol='ikRPsolver')  # Create IK handle
            cmds.circle(n=ikCtrl, r=8,
                        nr=self.normal[primaryAxis - 1])  # Create IK controller and position it on the joint

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

            l_IkFkSwitchPosition = cmds.xform(self.l_arm_ikJoints[2], q=1, ws=1, rp=1)
            l_IkFkSwitchPosition[2] = l_IkFkSwitchPosition[2] - 20
            r_IkFkSwitchPosition = cmds.xform(self.r_arm_ikJoints[2], q=1, ws=1, rp=1)
            r_IkFkSwitchPosition[2] = r_IkFkSwitchPosition[2] - 20

            if side is left:
                cmds.xform(cmds.curve(n=side + 'IK_FK_switch', d=True, p=self.IKFK_switchCtrlPoints,
                                      k=self.IKFK_switchCtrlPCount), t=l_IkFkSwitchPosition)
                changeShapeColor(side + 'IK_FK_switch', 18)
            if side is right:
                cmds.xform(cmds.curve(n=side + 'IK_FK_switch', d=True, p=self.IKFK_switchCtrlPoints,
                                      k=self.IKFK_switchCtrlPCount), t=r_IkFkSwitchPosition)
                changeShapeColor(side + 'IK_FK_switch', 18)

            cmds.addAttr(longName=side + 'IK_FK_switch', attributeType='double', min=0, max=1, defaultValue=0)
            cmds.setAttr(side + 'IK_FK_switch' + '.' + side + 'IK_FK_switch', edit=True, keyable=True)
            cmds.makeIdentity(side + 'IK_FK_switch', apply=True)
            cmds.delete(side + 'IK_FK_switch', constructionHistory=True)

            arm_ik_pos = cmds.xform(side + 'upperArm_IK_jnt', q=True, ws=True,
                                    t=True)  # Query positions in space of the IK joints and feed them
            elbow_ik_pos = cmds.xform(side + 'foreArm_IK_jnt', q=True, ws=True,
                                      t=True)  # to the function, so you can convert them in vectors
            wrist_ik_pos = cmds.xform(side + 'hand_IK_jnt', q=True, ws=True, t=True)

            self.getPVctrlPosition(arm_ik_pos, elbow_ik_pos, wrist_ik_pos, side)

            cmds.makeIdentity(side + 'elbow_ctrl', apply=True)
            cmds.delete(side + 'elbow_ctrl', constructionHistory=True)
            cmds.group(name=side + 'elbow_ctrl' + '_offset')
            cmds.matchTransform(cmds.poleVectorConstraint(side + 'elbow_ctrl', ikName), side + 'hand_IK_jnt')

            cmds.shadingNode('reverse', asUtility=True, name=side + 'IkFkReverse')
            cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', side + 'IkFkReverse.inputX')

            if side is left:
                for a, b, f in zip(self.l_arm_joints, self.l_arm_ikJoints, self.l_arm_fkJoints):
                    cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch',
                                     a + '_parentConstraint1.' + b + 'W1', force=True)
                    cmds.connectAttr(side + 'IkFkReverse.outputX', a + '_parentConstraint1.' + f + 'W0', force=True)
            elif side is right:
                for a, b, f in zip(self.r_arm_joints, self.r_arm_ikJoints, self.r_arm_fkJoints):
                    cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch',
                                     a + '_parentConstraint1.' + b + 'W1', force=True)
                    cmds.connectAttr(side + 'IkFkReverse.outputX', a + '_parentConstraint1.' + f + 'W0', force=True)

            cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch',
                             side + 'arm_ikHandle_ctrl_offset.visibility', force=True)
            cmds.connectAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', side + 'elbow_ctrl_offset.visibility',
                             force=True)
            cmds.connectAttr(side + 'IkFkReverse.outputX', side + 'upperArm_FK_offset.visibility', force=True)

        def createFootCtrl(footCtrl, side):

            def selectMoveCurvePoints(curvePoint, x, y, z):
                cmds.select(curvePoint, r=True)
                cmds.xform(curvePoint, r=True, t=[x, y, z])
                cmds.select(deselect=True)

            if side is left:
                cmds.circle(n=side + footCtrl, c=[0, 0, 0], nr=[0, 1, 0], sw=360, r=15, d=3, ut=0, tol=0.01, s=8, ch=1)

                selectMoveCurvePoints(side + footCtrl + '.cv[3]', 13, 0, 0)
                selectMoveCurvePoints(side + footCtrl + '.cv[0]', -6.5, 0, 0)
                selectMoveCurvePoints(side + footCtrl + '.cv[7]', -8, 0, 0)
                selectMoveCurvePoints(side + footCtrl + '.cv[2]', 1.5, 0, 0)
                selectMoveCurvePoints(side + footCtrl + '.cv[4]', 1.5, 0, 0)

                cmds.matchTransform(side + footCtrl, side + 'toe_jnt', px=True, pz=True)
                cmds.makeIdentity(side + footCtrl, apply=True)
                cmds.delete(side + footCtrl, constructionHistory=True)
                cmds.group(side + footCtrl, name=side + footCtrl + '_offset')
                cmds.select(deselect=True)
                movePivot('l_foot_ctrl_offset', 'l_ankle_jnt')
                movePivot('l_foot_ctrl', 'l_ankle_jnt')

            if side is right:
                cmds.duplicate('l_foot_ctrl_offset', name='r_foot_ctrl_offset')
                cmds.select('r_foot_ctrl_offset', hi=True)
                cmds.ls(sl=True)
                cmds.rename(cmds.ls(sl=True)[1], 'r_foot_ctrl')
                movePivot('r_foot_ctrl_offset', 'world')
                cmds.setAttr('r_foot_ctrl_offset.scaleX', -1)
                movePivot('r_foot_ctrl_offset', 'r_ankle_jnt')
                movePivot('r_foot_ctrl', 'r_ankle_jnt')

        def footRoll(side):

            def channelControl(sameSide, channel):
                cmds.select(sameSide + channel)
                cmds.setAttr(sameSide + channel + '.scaleX', k=False)
                cmds.setAttr(sameSide + channel + '.scaleY', k=False)
                cmds.setAttr(sameSide + channel + '.scaleZ', k=False)
                cmds.setAttr(sameSide + channel + '.translateX', k=False)
                cmds.setAttr(sameSide + channel + '.translateY', k=False)
                cmds.setAttr(sameSide + channel + '.translateZ', k=False)
                cmds.setAttr(sameSide + channel + '.rotateAxisX', k=True)

            def setKey(sameSide):
                cmds.setDrivenKeyframe(sameSide + 'heelRoll.rotateAxisX',
                                       currentDriver=sameSide + 'foot_ctrl' + '.' + sameSide + 'footRoll')
                cmds.setDrivenKeyframe(sameSide + 'toeRoll.rotateAxisX',
                                       currentDriver=sameSide + 'foot_ctrl' + '.' + sameSide + 'footRoll')
                cmds.setDrivenKeyframe(sameSide + 'ballRoll.rotateAxisX',
                                       currentDriver=sameSide + 'foot_ctrl' + '.' + sameSide + 'footRoll')

            cmds.select(side + 'foot_ctrl')
            cmds.addAttr(longName=side + 'footRoll', attributeType='double', min=-10, max=10, defaultValue=0)
            cmds.setAttr(side + 'foot_ctrl' + '.' + side + 'footRoll', e=True, keyable=True)

            channelControl(side, 'heelRoll')
            channelControl(side, 'toeRoll')
            channelControl(side, 'ballRoll')

            cmds.select(side + 'heelRoll')
            cmds.select(side + 'toeRoll', add=True)
            cmds.select(side + 'ballRoll', add=True)

            cmds.setAttr(side + 'foot_ctrl' + '.' + side + 'footRoll', -10)
            cmds.setAttr(side + 'heelRoll.rotateAxisX', -50)
            setKey(side)

            cmds.setAttr(side + 'foot_ctrl' + '.' + side + 'footRoll', 0)
            cmds.setAttr(side + 'heelRoll.rotateAxisX', 0)
            setKey(side)

            cmds.setAttr(side + 'foot_ctrl' + '.' + side + 'footRoll', 5)
            cmds.setAttr(side + 'ballRoll.rotateAxisX', 50)
            setKey(side)

            cmds.setAttr(side + 'foot_ctrl' + '.' + side + 'footRoll', 10)
            cmds.setAttr(side + 'toeRoll.rotateAxisX', 50)
            cmds.setAttr(side + 'ballRoll.rotateAxisX', 0)
            setKey(side)

            cmds.setAttr(side + 'ballRoll.rotateAxisX', 0)
            cmds.setAttr(side + 'foot_ctrl' + '.' + side + 'footRoll', 0)
            setKey(side)
            cmds.select(d=True)

        def leg_ikControls(side):

            ikLegName = side + 'leg_ikHandle'
            ikHeelName = side + 'heel_ikHandle'
            ikToeName = side + 'toe_ikHandle'

            if side is left:
                cmds.ikHandle(name=ikLegName, startJoint=self.l_leg_ikJoints[0], endEffector=self.l_leg_ikJoints[2],
                              sol='ikRPsolver')  # Create leg IK handle
                cmds.ikHandle(name=ikHeelName, startJoint='l_ankle_jnt', endEffector='l_toe_jnt',
                              sol='ikRPsolver')  # Create heel IK handle
                cmds.ikHandle(name=ikToeName, startJoint='l_toe_jnt', endEffector='l_toeNub_jnt',
                              sol='ikRPsolver')  # Create toe IK handle
                cmds.group(name='l_toeGrp')
                cmds.group(name='l_ballRoll')
                cmds.group(name='l_toeRoll')
                cmds.group(name='l_heelRoll')
                cmds.parent('l_toeGrp', 'l_toeRoll')
                cmds.parent('l_leg_ikHandle', 'l_ballRoll')
                cmds.parent('l_heel_ikHandle', 'l_ballRoll')
                cmds.parent('l_heelRoll', 'l_foot_ctrl')
                movePivot('l_heelRoll', 'l_foot_ctrlShape.cv[1]')
                movePivot('l_toeRoll', 'l_toeNub_jnt')
                movePivot('l_toeGrp', 'l_toe_jnt')
                movePivot('l_ballRoll', 'l_toe_jnt')

            elif side is right:
                cmds.ikHandle(name=ikLegName, startJoint=self.r_leg_ikJoints[0], endEffector=self.r_leg_ikJoints[2],
                              sol='ikRPsolver')  # Create leg IK handle
                cmds.ikHandle(name=ikHeelName, startJoint='r_ankle_jnt', endEffector='r_toe_jnt',
                              sol='ikRPsolver')  # Create heel IK handle
                cmds.ikHandle(name=ikToeName, startJoint='r_toe_jnt', endEffector='r_toeNub_jnt',
                              sol='ikRPsolver')  # Create toe IK handle
                cmds.group(name='r_toeGrp')
                cmds.group(name='r_ballRoll')
                cmds.group(name='r_toeRoll')
                cmds.group(name='r_heelRoll')
                cmds.parent('r_toeGrp', 'r_toeRoll')
                cmds.parent('r_leg_ikHandle', 'r_ballRoll')
                cmds.parent('r_heel_ikHandle', 'r_ballRoll')
                cmds.parent('r_heelRoll', 'r_foot_ctrl')
                movePivot('r_heelRoll', 'r_foot_ctrlShape.cv[1]')
                movePivot('r_toeRoll', 'r_toeNub_jnt')
                movePivot('r_toeGrp', 'r_toe_jnt')
                movePivot('r_ballRoll', 'r_toe_jnt')

            thigh_ik_pos = cmds.xform(side + 'thigh_IK_jnt', q=True, ws=True,
                                      t=True)  # Query positions in space of the IK joints and feed them
            calf_ik_pos = cmds.xform(side + 'calf_IK_jnt', q=True, ws=True,
                                     t=True)  # to the function, so you can convert them in vectors
            ankle_ik_pos = cmds.xform(side + 'ankle_IK_jnt', q=True, ws=True, t=True)

            self.getPVkneeCtrlPosition(thigh_ik_pos, calf_ik_pos, ankle_ik_pos, side)

            cmds.makeIdentity(side + 'knee_ctrl', apply=True)
            cmds.delete(side + 'knee_ctrl', constructionHistory=True)
            cmds.group(name=side + 'knee_ctrl' + '_offset')
            cmds.matchTransform(cmds.poleVectorConstraint(side + 'knee_ctrl', ikLegName), side + 'ankle_IK_jnt')

        dropdown = cmds.optionMenuGrp('optMenu', query=True, sl=True) - 1

        if dropdown == 0:

            arm_ikControls(left)
            arm_ikControls(right)

        elif dropdown == 1:

            createFootCtrl('foot_ctrl', left)
            createFootCtrl('foot_ctrl', right)
            leg_ikControls(left)
            leg_ikControls(right)
            footRoll(left)
            footRoll(right)
            cmds.makeIdentity('r_heelRoll', apply=True)
            cmds.orientConstraint('l_foot_ctrl', 'l_ankle_IK_jnt', mo=True)
            cmds.orientConstraint('r_foot_ctrl', 'r_ankle_IK_jnt', mo=True)
            cmds.parent('l_knee_ctrl_offset', 'l_foot_ctrl')
            cmds.parent('r_knee_ctrl_offset', 'r_foot_ctrl')
            cmds.select(d=True)

        #    legGroups = ['l_leg', 'r_leg']
        #    legJoints = ['l_thigh_jnt', 'r_thigh_jnt']

        #    for i, j in zip(legGroups, legJoints):
        #        cmds.group(em=True, name=i)
        #        cmds.xform(i, cp=True)
        #        cmds.matchTransform(i, j)
        #        cmds.makeIdentity(i, apply=True, translate=True)
        #        cmds.delete(i, constructionHistory=True)
        #        cmds.parent(j, i)
        #    cmds.parent('l_thigh_IK_jnt', 'l_leg')
        #    cmds.parent('r_thigh_IK_jnt', 'r_leg')

    def connectComponents(self, args):

        def connectLegs():

            cmds.parent('l_thigh_jnt', 'pelvis_jnt')
            cmds.parent('r_thigh_jnt', 'pelvis_jnt')
            cmds.parent(self.l_leg_ikJoints[0], 'pelvis_jnt')
            cmds.parent(self.r_leg_ikJoints[0], 'pelvis_jnt')
            cmds.parentConstraint('waist_ctrl', 'l_thigh_jnt', maintainOffset=True)
            cmds.parentConstraint('waist_ctrl', 'r_thigh_jnt', maintainOffset=True)
            cmds.select(d=True)

        def connectArms():

            cmds.parent(self.l_arm_ikJoints[0], 'l_clavicle_jnt')
            cmds.parent(self.l_arm_fkJoints[0], 'l_clavicle_jnt')
            cmds.parent(self.r_arm_ikJoints[0], 'r_clavicle_jnt')
            cmds.parent(self.r_arm_fkJoints[0], 'r_clavicle_jnt')

            cmds.parent('l_clavicle_jnt', 'neck01_jnt')
            cmds.parent('r_clavicle_jnt', 'neck01_jnt')
            cmds.select(d=True)

        def connectEyes():

            cmds.parent('l_eye_jnt', 'head_jnt')
            cmds.parent('r_eye_jnt', 'head_jnt')

        def connectJaw():

            cmds.parent('jaw_jnt', 'head_jnt')
            cmds.parent('jaw_offset', 'head_ctrl')

        def rigControls():

            cmds.spaceLocator(name='loc')
            rigController = 'rig_ctrl'  # Create spine control
            cmds.xform(cmds.curve(name=rigController, d=True, p=self.spine_Ctrl_Points, k=self.spine_Ctrl_PCount), cp=True)
            cmds.select(d=True)

            cmds.matchTransform(rigController, 'loc', px=True, pz=True, pos=True)
            cmds.scale(0.12, 0.12, 0.12, rigController, absolute=True)
            changeShapeColor(rigController, 18)

            cmds.group(rigController, name=rigController + '_offset')
            cmds.makeIdentity(rigController, apply=True)
            cmds.delete(rigController, constructionHistory=True)
            cmds.makeIdentity('rig_ctrl_offset', apply=True)
            cmds.delete('rig_ctrl_offset', constructionHistory=True)
            cmds.delete('loc')

            rootController = 'root_ctrl'
            cmds.circle(n=rootController, r=30, nr=self.normal[1])
            changeShapeColor(rootController, 14)
            cmds.group(rootController, name=rootController + '_offset')
            cmds.makeIdentity(rootController, apply=True)
            cmds.delete(rootController, constructionHistory=True)
            cmds.makeIdentity('root_ctrl_offset', apply=True)
            cmds.delete('root_ctrl_offset', constructionHistory=True)
            cmds.parent('root_ctrl_offset', 'rig_ctrl')

            cmds.joint()
            cmds.joint(name='root_jnt', e=True, oj='none', ch=True, zso=True)
            cmds.parent('pelvis_jnt', 'root_jnt')
            cmds.parent('root_jnt', 'joints')
            cmds.parentConstraint('root_ctrl', 'root_jnt', mo=True)

        def connectControls():

            cmds.parent('l_clavicle_offset', 'neck01_ctrl')
            cmds.parent('r_clavicle_offset', 'neck01_ctrl')
            cmds.select(d=True)
            cmds.select('l_fingers_ctrl_offset', 'r_fingers_ctrl_offset', 'l_arm_ikHandle_ctrl_offset',
                        'r_arm_ikHandle_ctrl_offset', 'l_elbow_ctrl_offset', 'r_elbow_ctrl_offset',
                        'l_foot_ctrl_offset', 'r_foot_ctrl_offset', 'spine_ctrl_offset', 'eye_ctrl_offset',
                        'l_IK_FK_switch', 'r_IK_FK_switch', add=True)
            controls = cmds.ls(sl=True)
            for i in controls:
                cmds.parent(i, 'root_ctrl')

            cmds.parent('rig_ctrl_offset', 'controls')

        cmds.select(d=True)
        cmds.group(em=True, name='rig')
        cmds.group(em=True, name='joints')
        cmds.group(em=True, name='controls')

        cmds.parent('joints', 'rig')
        cmds.parent('controls', 'rig')

        deleteAllLocators(args=True)

        connectLegs()
        connectArms()
        connectEyes()
        connectJaw()
        rigControls()
        connectControls()

        cmds.select(d=True)

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

        arm_fk_pos = cmds.xform(side + 'upperArm_FK_jnt', q=True, ws=True,
                                t=True)  # Query positions in space of the IK joints and feed them
        elbow_fk_pos = cmds.xform(side + 'foreArm_FK_jnt', q=True, ws=True,
                                  t=True)  # to the function, so you can convert them in vectors
        wrist_fk_pos = cmds.xform(side + 'hand_FK_jnt', q=True, ws=True, t=True)

        if cmds.getAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch') == 1:
            cmds.matchTransform(side + 'upperArm_FK_ctrl', side + 'upperArm_jnt')
            cmds.matchTransform(side + 'foreArm_FK_ctrl', side + 'foreArm_jnt')
            cmds.matchTransform(side + 'hand_FK_ctrl', side + 'hand_jnt')
            cmds.setAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', 0)

        elif cmds.getAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch') == 0:
            self.setPVctrlPosition(arm_fk_pos, elbow_fk_pos, wrist_fk_pos, side)
            cmds.setAttr(side + 'IK_FK_switch.' + side + 'IK_FK_switch', 1)

    def setXYZp(self, args):  # Radio buttons logic
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
