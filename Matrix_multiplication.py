#!/usr/bin/env python3

import numpy as np
A=np.array([[1,2],[1,3]])
B=np.array([2,1])
C=A@B.T
print(C)
