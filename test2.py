import maya.cmds as cmds

array = ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx']

a = ['x', 'y', 'z']
b = ['up', 'down']

r1 = 2
r2 = 2
r3 = 1
r4 = 2

sel = a[r1-1] + a[r2-1]

allAxis = ''
for i in array:
    if sel in i:
        if a[r1-1] == i[0]:
            allAxis = i

secAxis =  a[r3-1] + b[r4-1]

print(allAxis)
print(secAxis)
