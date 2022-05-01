import maya.cmds as cmds


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


def orientJoints():

    def findNub():
        for each in orient:  # thus automatically aligning correctly
            if cmds.listRelatives(each) is None:
                cmds.joint(each, e=True, oj='none', ch=True, zso=True)
            else:
                cmds.joint(each, e=True, oj=allAxis, sao=secAxis, ch=True, zso=True)


    xyz = ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx']  # List with all possible combinations for primary axis orientation
    a = ['x', 'y', 'z']
    b = ['up', 'down']

    r1 = 1
    r2 = 2
    r3 = 1
    r4 = 1

    sel = a[r1 - 1] + a[r2 - 1]  # Querying the radio buttons and setting the desired axis from list 'a'
    allAxis = ''  # The radio buttons produce integers that correspond to the letters of each radio button
    for i in xyz:  # The corresponding letters are then taken from list 'a', concatenated and compared against
        if sel in i[:2]:  # list 'xyz'. The matching string is assigned to 'allAxis', which defines the orientation
            allAxis = i  # of the primary axis

    secAxis = a[r3 - 1] + b[r4 - 1]  # Querying r3 and b to establish orientation for the secondary axis

    cmds.select(hi=True)  # Selecting all joints in the hierarchy
    orient = cmds.ls(sl=True)  # and storing their names in here
    findNub()

    c = []  # that is created (the thumb), which is wrong in the case of the hand. Rather, it needs to
    for i in orient:  # be aligned with the elbow (the world) - that can only happen if it has no children.
        c.append(cmds.joint(i, q=True, o=True))  # Creating the joints and a list with their orientations

    for i in c:  # if any of the xyz orientations equals 180, it means the joint has flipped
        for j in i:  # the following code corrects that with setting the appropriate secondary axis orientation
            if round(j) == 180:
                if cmds.xform(orient[1], q=1, ws=1, rp=1)[0] > cmds.xform(orient[0], q=1, ws=1, rp=1)[0]:  # If X value on the second joint in the hierarchy
                    if r3 == 3:  # is greater than X value of the first joint:
                        secAxis = a[r3 - 1] + b[r4 - 1]
                    else:
                        secAxis = a[r3 - 3] + b[r4 - 1]
                if cmds.xform(orient[1], q=1, ws=1, rp=1)[1] > cmds.xform(orient[0], q=1, ws=1, rp=1)[1]:  # If Y value on the second joint in the hierarchy                if r3 == 3:  # is greater than Y value of the first joint:
                    if r3 == 3:  # is greater than Y value of the first joint:
                        secAxis = a[r3 - 1] + b[r4 - 1]
                    else:
                        secAxis = a[r3 - 2] + b[r4 - 1]
    findNub()

orientJoints()