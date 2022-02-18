import sys
import os
sys.path.append(os.path.abspath("C:/Users/fresh/PycharmProjects/AutoRigging"))
import maya.cmds as cmds






x = cmds.ls(sl=True)                                    # Change rotation order for the selected joint
for i in x:
    cmds.setAttr(i + '.rotateOrder', 0)


x = cmds.ls(sl=True)                                    # Enable stretching for the selected joint
for i in x:
    cmds.setAttr(i + '.segmentScaleCompensate', 1)


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