import maya.cmds as cmds


def setXYZp(args):
    a = cmds.radioButtonGrp(radioGroup1, q=True, sl=True)
    b = cmds.radioButtonGrp(radioGroup2, q=True, sl=True)
    if a == 1 and b == 1:
        cmds.radioButtonGrp(radioGroup2, e=True, sl=2)
    elif a == 2 and b == 2:
        cmds.radioButtonGrp(radioGroup2, e=True, sl=3)
    elif a == 3 and b == 3:
        cmds.radioButtonGrp(radioGroup2, e=True, sl=1)

def setXYZs(args):
    a = cmds.radioButtonGrp(radioGroup1, q=True, sl=True)
    b = cmds.radioButtonGrp(radioGroup2, q=True, sl=True)
    if b == 1 and a == 1:
        cmds.radioButtonGrp(radioGroup1, e=True, sl=2)
    elif b == 2 and a == 2:
        cmds.radioButtonGrp(radioGroup1, e=True, sl=3)
    elif b == 3 and a == 3:
        cmds.radioButtonGrp(radioGroup1, e=True, sl=1)

def checkboxState(args):
    if cmds.checkBox(checkbox1, q=True, v=True) == 1:
        cmds.columnLayout(layout2, e=True, en=0)
    elif cmds.checkBox(checkbox1, q=True, v=True) == 0:
        cmds.columnLayout(layout2, e=True, en=1)

def values(args):
    print(cmds.radioButtonGrp(radioGroup1, query=True, sl=True))
    print(cmds.radioButtonGrp(radioGroup2, query=True, sl=True))
    print(cmds.radioButtonGrp(radioGroup3, query=True, sl=True))

radioWindow = cmds.window(title="Spawn Joints", widthHeight=(470, 250))
layout1 = cmds.columnLayout(adjustableColumn=True, ebg=True)
layout3 = cmds.columnLayout(parent=layout1, cw=470, cat=('both', 142))

checkbox1 = cmds.checkBox(label='Orient To World', value=0, onc=checkboxState, ofc=checkboxState, parent=layout3)

layout2 = cmds.columnLayout(adjustableColumn=True, ebg=True, parent=layout1)
radioGroup1 = cmds.radioButtonGrp(nrb=3, label='Primary Axis', labelArray3=['X', 'Y', 'Z'], cw=([2,70], [3,70]), sl=1, p=layout2, on1=setXYZp, on2=setXYZp, on3=setXYZp)
radioGroup2 = cmds.radioButtonGrp(nrb=4, label='Secondary Axis', labelArray4=['X', 'Y', 'Z', 'None'], cw=([2,70], [3,70], [4,70]), sl=2, p=layout2, on1=setXYZs, on2=setXYZs, on3=setXYZs)
radioGroup3 = cmds.radioButtonGrp(nrb=3, label='World Orientation', labelArray3=['X', 'Y', 'Z'], cw=([2,70], [3,70], [4,70]), sl=2, p=layout2)
cmds.optionMenuGrp('updown', parent=radioGroup3)

cmds.menuItem(label='+')
cmds.menuItem(label='-')
cmds.button(label='Print Values', command=values, parent=layout1)
cmds.button(label='Close', command=('cmds.deleteUI(\"' + radioWindow + '\", window=True)'), parent=layout1)

cmds.showWindow(radioWindow)

'''

y=[]                                                    # Parent all fingers to hand joint
for eachlist in handLoc:
    y.append(eachlist[0].replace('_loc', '_jnt'))
for i in y:
    cmds.connectJoint(i, 'l_hand_jnt', pm=True)

cmds.connectJoint('l_thigh_jnt', 'pelvis_jnt', pm=True) # Parent the rest of the chains
cmds.connectJoint('l_clavicle_jnt', 'spine04_jnt', pm=True)
cmds.connectJoint('jaw_jnt', 'head02_jnt', pm=True)
cmds.connectJoint('l_eye_jnt', 'head02_jnt', pm=True)

'''