# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:49:21 2024

@author: s_reitz20
"""

import numpy as np
E = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[9,8,7], [6,5,4], [3,2,1]], [[9,8,7], [3,2,1], [6,5,4]]])
print(E)
print(E.sum(axis = (1,2))) # es müssen zwei Parameter geliefert werden, weil immer alle Scheiben addiert werden sollen


