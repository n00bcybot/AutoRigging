import maya.cmds as cmds

left = 'l_'
right = 'r_'



def footRoll(side):

    def chanelControl(side, chanel):
        cmds.select(side + chanel)
        cmds.setAttr(side + chanel + '.scaleX', k=False)
        cmds.setAttr(side + chanel + '.scaleY', k=False)
        cmds.setAttr(side + chanel + '.scaleZ', k=False)
        cmds.setAttr(side + chanel + '.translateX', k=False)
        cmds.setAttr(side + chanel + '.translateY', k=False)
        cmds.setAttr(side + chanel + '.translateZ', k=False)
        cmds.setAttr(side + chanel + '.rotateAxisX', k=True)

    def setKey(side):
        cmds.setDrivenKeyframe(side + 'heelRoll.rotateAxisX', currentDriver=side + 'foot_ctrl' + '.' + side + 'footRoll')
        cmds.setDrivenKeyframe(side + 'toeRoll.rotateAxisX', currentDriver=side + 'foot_ctrl' + '.' + side + 'footRoll')
        cmds.setDrivenKeyframe(side + 'ballRoll.rotateAxisX', currentDriver=side + 'foot_ctrl' + '.' + side + 'footRoll')

    cmds.select(side + 'foot_ctrl')
    cmds.addAttr(longName=side + 'footRoll', attributeType='double', min=-10, max=10, defaultValue=0)
    cmds.setAttr(side + 'foot_ctrl' + '.' + side + 'footRoll', e=True, keyable=True)

    chanelControl(side, 'heelRoll')
    chanelControl(side, 'toeRoll')
    chanelControl(side, 'ballRoll')

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

footRoll(left)
footRoll(right)
'''    


    setAttr  "l_foot_ctrl.FootRoll" 5;
    setDrivenKeyframe - currentDriver  l_foot_ctrl.FootRoll l_heelRoll.rotateAxisX;
    setDrivenKeyframe - currentDriver l_foot_ctrl.FootRoll l_toeRoll.rotateAxisX;
    setAttr "l_ballRoll.rotateAxisX" 50;
    setDrivenKeyframe - currentDriver  l_foot_ctrl.FootRoll l_ballRoll.rotateAxisX;
    setAttr "l_foot_ctrl.FootRoll"  10;
    setDrivenKeyframe - currentDriver l_foot_ctrl.FootRoll  l_heelRoll.rotateAxisX;
    setAttr "l_toeRoll.rotateAxisX" 50;
    setDrivenKeyframe - currentDriver l_foot_ctrl.FootRoll  l_toeRoll.rotateAxisX;
    setAttr "l_ballRoll.rotateAxisX" 0;
    setDrivenKeyframe - currentDriver l_foot_ctrl.FootRoll l_ballRoll.rotateAxisX;
'''