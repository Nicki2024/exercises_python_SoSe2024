# -*- coding: utf-8 -*-
"""
Created on Fri May 24 13:03:34 2024

@author: s_reitz20
"""
import numpy as np

#Übung 1

a= np.arange(1, 13)
print(a)

a_3d = a.reshape(3,2,2)
print(a_3d)



#Übung 2

#print(np.ndim(a_3d))
#print(np.shape(a_3d))
#print(np.size(a_3d))
#print(np.dtype(a_3d))

#oder besser:

print(a_3d.shape)
print(a_3d.ndim)
print(a_3d.size)
print(a_3d.dtype)