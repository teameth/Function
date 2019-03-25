#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import random
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
# names为需要做图的节点名称
# vec为名称对应的向量
# label为标签的list
# accountDict为节点对应类型的dict
def Visualize(names, vec, label, accountDict):
	node_color = []
	node_size = []
	# 决定节点的大小和颜色
	for line in names:
		if line in label:
			node_color.append('r')
			node_size.append(int(45))
		elif accountDict.get(line)=='Sc':
			node_color.append('g')
			node_size.append(int(10))
		elif accountDict.get(line)=='No':
			node_color.append('b')
			node_size.append(int(10))

	types = ['random', 'pca']
	start_time = time.time()
	for type in types:
		# 降维
		two_dim_vec = TSNE(n_components=2, init=type, perplexity = 40, early_exaggeration = 24).fit_transform(vec)
		plt.figure(figsize=(50,20))
		plt.scatter(two_dim_vec[:, 0], two_dim_vec[:, 1], s = node_size, c = node_color)
		plt.savefig('figNew '+ type +'.png')
		# plt.show()
	print('tSNE done, elapsed time: {}'.format(round(time.time()-start_time)))

