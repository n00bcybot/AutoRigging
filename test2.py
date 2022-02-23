import maya.cmds as cmds


def printValues():
    xyz = ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx']

    a = ['x', 'y', 'z']
    b = ['up', 'down']

    r1 = 1
    r2 = 2
    r3 = 2
    r4 = 1

    sel = a[r1 - 1] + a[r2 - 1]

    allAxis = ''
    for i in xyz:
        if sel in i:
            if a[r1 - 1] == i[0]:
                allAxis = i

    secAxis = a[r3 - 1] + b[r4 - 1]

    print(allAxis)
    print(secAxis)
    cmds.joint(e=True, oj=allAxis, sao=secAxis, ch=True, zso=True)

printValues()
