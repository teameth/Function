#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def nametoVecDict(filepath):
    labelMat = []
    disMat = []
    vector = []
    fr = open(filepath, 'rb')
    for line in fr.readlines():
        lineArr = line.strip().split()
        disMat = []
        for k in range(1, lineArr.__len__()):
            disMat.append(float(lineArr[k]))
        labelMat.append(str(lineArr[0], encoding = "utf-8"))
        vector.append(disMat)
    fr.close()
    find = dict(zip(labelMat, vector))
    return find