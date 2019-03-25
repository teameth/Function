#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import random
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
# fingVec为name对应vec的词典
# vecpath为embedding结果的文件路径
# label为标签的list
def CalculateNeighbor(findVec, vecpath, label):
	vec = []
	names = []
	result = []
	data = []
	count = 0
	for i in label:
		if i in findVec.keys():
			count = count + 1
			a1 = np.array(findVec.get(i))
			fr2 = open(vecpath, 'rb')
			print(str(count) + ":" + i)
			data = []
			result = []
			sortMat = []
			for line in fr2.readlines():
				lineArr=line.strip().split()
				data = []
				for k in range(1, lineArr.__len__()):
					data.append(float(lineArr[k]))
				label = (str(lineArr[0], encoding = "utf-8"))
				a2 = np.array(data)
				dist = np.linalg.norm(a2 - a1)
				sortMat.append((dist,label))
			result = sorted(sortMat)
			for k in range(1200):
				if k < len(result):
					if str(result[k][1]) in names:
						continue
					else:
						names.append(str(result[k][1]))
						vec.append(findVec.get(str(result[k][1])))
	return names,vec