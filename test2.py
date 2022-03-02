import maya.cmds as cmds


def printValues():

    def findNub():
        cmds.select(hi=True)
        joint = cmds.ls(sl=True)
        for i in joint:
            if cmds.listRelatives(i) is None:
                cmds.joint(i, e=True, oj='none', ch=True, zso=True)
            else:
                cmds.joint(i, e=True, oj=allAxis, sao=secAxis, ch=True, zso=True)

    xyz = ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx']
    a = ['x', 'y', 'z']
    b = ['up', 'down']

    r1 = 3
    r2 = 2
    r3 = 1
    r4 = 1

    sel = a[r1 - 1] + a[r2 - 1]
    allAxis = ''
    for i in xyz:
        if sel in i[:2]:
            allAxis = i
    print(allAxis)
    secAxis = a[r3 - 1] + b[r4 - 1]

    findNub()
    cmds.select(hi=True)
    orient = cmds.ls(sl=True)
    print(orient)
    c = []
    for i in orient:
        c.append(cmds.joint(i, q=True, o=True))
    for i in c:
        for j in i:
            if round(j) == 180:
                if cmds.xform(orient[1], q=1, ws=1, rp=1)[0] > cmds.xform(orient[0], q=1, ws=1, rp=1)[0]:
                    if r3 == 3:
                        secAxis = a[r3 - 1] + b[r4 - 1]
                    else:
                        secAxis = a[r3 - 3] + b[r4 - 1]
                if cmds.xform(orient[1], q=1, ws=1, rp=1)[1] > cmds.xform(orient[0], q=1, ws=1, rp=1)[1]:
                    if r3 == 3:
                        secAxis = a[r3 - 1] + b[r4 - 1]
                    else:
                        secAxis = a[r3 - 2] + b[r4 - 1]
    findNub()


printValues()
