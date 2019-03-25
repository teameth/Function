#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
def readLabel(filepath, k):
	key=[]
	need_name = pd.read_csv(filepath, header = None)
	key = need_name[k].tolist()
	return key