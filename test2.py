import maya.cmds as cmds


def getCurvePoints():
    curve = cmds.ls(sl=True)[0]
    curvePointsPositions = cmds.getAttr(curve + '.cv[*]')
    pointsCount = []
    for i in range(len(curvePointsPositions)):
        pointsCount.append(i)
    print(curvePointsPositions)
    print(pointsCount)

# cmds.curve(d=True, p=curvePointsPositions, k=pointsCount) # Create curve


getCurvePoints()
