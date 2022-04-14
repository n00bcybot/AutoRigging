import maya.cmds as cmds

left = 'l_'
right = 'r_'


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

def movePivot(object, joint):

    world = [0,0,0]

    def getJointWP(joint):
        cmds.spaceLocator()
        locator = cmds.ls(sl=True)[0]
        cmds.matchTransform(locator, joint)
        pointWP = cmds.xform(locator, q=True, t=True)
        cmds.delete(locator)
        return pointWP

    if joint is 'world':
        pointWP = world
    else:
        pointWP = getJointWP(joint)

    x = pointWP[0]
    y = pointWP[1]
    z = pointWP[2]

    cmds.move(x, y, z, object + '.scalePivot', object + '.rotatePivot')

createFootCtrl('foot_ctrl', left)
createFootCtrl('foot_ctrl', right)


