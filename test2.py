import maya.cmds as cmds

def getJointWP(joint):
    cmds.spaceLocator()
    locator = cmds.ls(sl=True)[0]
    cmds.matchTransform(locator, joint)
    jointWP = cmds.xform(locator, q=True, t=True)
    cmds.delete(locator)
    return jointWP

def getDirection():

    joint1 = getJointWP('joint1')
    joint2 = getJointWP('joint2')

    number = []
    for i, j in zip(joint2, joint1):
        number.append(abs((i) - (j)))

    for i in number:
        if i == max(number):
            if number.index(i) == 0:
                print('Directon is X')
                return 1
            elif number.index(i) == 1:
                print('Directon is Y')
                return 2
            elif number.index(i) == 2:
                print('Directon is Z')
                return 3

def findNub():  # This function checks whether the joint that needs to be orientated is at the end of the chain, as in, it has no children
    # If it has no children, it will be oriented to the world (meaning it will inherit orientation from the parent joint)
    for each in orient:  # thus automatically aligning correctly
        if cmds.listRelatives(each) is None:
            cmds.joint(each, e=True, oj='none', ch=True, zso=True)
        else:
            cmds.joint(each, e=True, oj=allAxis, sao=secAxis, ch=True, zso=True)

direction = getDirection()
xyz = ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx']  # List with all possible combinations for primary axis orientation
a = ['x', 'y', 'z']
b = ['up', 'down']

r1 = 3
r2 = 2
r3 = 3
r4 = 1

sel = a[r1 - 1] + a[r2 - 1]  # Querying the radio buttons and setting the desired axis from list 'a'
allAxis = ''                # The radio buttons produce integers that correspond to the letters of each radio button
for i in xyz:               # The corresponding letters are then taken from list 'a', concatenated and compared against
    if sel in i[:2]:        # list 'xyz'. The matching string is assigned to 'allAxis', which defines the orientation
        allAxis = i         # of the primary axis

secAxis = a[r3 - 1] + b[r4 - 1]  # Querying r3 and b to establish orientation for the secondary axis
print(secAxis)
cmds.select('joint1')
cmds.select(hi=True)    # Selecting all joints in the hierarchy
orient = cmds.ls(sl=True)  # and storing their names in here
findNub()
c = []                           # that is created (the thumb), which is wrong in the case of the hand. Rather, it needs to
y = []
for each in orient:                        # be aligned with the elbow (the world) - that can only happen if it has no children.
    c.append(cmds.joint(each, q=True, o=True))  # Creating the joints and a list with their orientations
for i in c:                                 # if any of the xyz orientations equals 180, it means the joint has flipped
    for j in i:                             # the following code corrects that with setting the appropriate secondary axis orientation
        y.append(round(abs(j)))
for i in y:
    if i == 180:
        if r3 == direction:
            if direction == 1:
                secAxis = a[r3 - 2] + b[r4 - 1]
            elif direction == 2:
                secAxis = a[r3] + b[r4 - 1]
            elif direction == 3:
                secAxis = a[r3 - 3] + b[r4 - 1]
print(secAxis)
findNub()
