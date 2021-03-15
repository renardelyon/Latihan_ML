#!/usr/bin/env python3

import numpy as np
import numpy.linalg as nla

A = np.array([[1,2,3],
		[3,1,2],
		[0,0,0]])
A=A/np.max(A)
B = np.array ([[4,5,6],
		[6,6,6]])
B= B/ np.max(B)
num_Point= A.shape[0]
num_Centroid = B.shape[0]
point_Norm = nla.norm(A,axis=1)
Centroid_Norm = nla.norm(B,axis=1)
point_Norm = np.reshape(point_Norm, (num_Point,1))
Centroid_Norm = np.reshape(Centroid_Norm,(1,num_Centroid))
print (point_Norm + Centroid_Norm - 2.0 * np.dot(point_Norm, Centroid_Norm))

