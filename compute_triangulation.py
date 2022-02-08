#!/usr/bin/env python

import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from face_tesselation_info import face_tesselation
preList = []
for tri in face_tesselation:
    preList.append(tri)
N = len(preList)
pre2List = []
for i in range(0, N, 3):
    pre2List.append(
    [preList[i][0], preList[i][1], 
    preList[i+1][0], preList[i+1][1], 
    preList[i+2][0], preList[i+2][1]]
    )
triList = []
for tri in pre2List:
    if  tri[1] != tri[2] or tri[3] != tri[4] or tri[5] != tri[0]:
        print('fail')

    triList.append( [tri[0], tri[1], tri[3]] )

f = open("./triangle.txt", 'w')
for tri in triList:
    txt = '%d %d %d \n' % (tri[0], tri[1], tri[2])
    f.write(txt)

f.close()