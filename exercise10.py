# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:36:39 2024

@author: s_reitz20
"""

import numpy as np
d = np.arange(1,11)
D = np.tile(d, (10,1))
print(D)

print(D.sum(axis = 0))

print(D.mean(axis = 1))