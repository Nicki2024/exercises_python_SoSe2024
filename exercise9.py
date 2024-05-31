# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:13:30 2024

@author: s_reitz20
"""

import numpy as np

M = np.eye(5,dtype = "int")
M[3:, :2] = 2
M[ :2, 3: ] = 3
print(M)

