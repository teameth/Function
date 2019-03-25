#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
def nametoType(filepath):
	fr = open(filepath, 'rb')
	accountDict = {}
	accountList = []
	accountType = []
	for accountLine in fr.readlines():
		Aline = str(accountLine, encoding = "utf-8")
		DictLineArr = Aline.strip().split(',')
		accountList.append(str(DictLineArr[1]))
		accountType.append(str(DictLineArr[2]))
	accountDict = dict(zip(accountList, accountType))
	return accountDict