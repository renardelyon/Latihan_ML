#!/usr/bin/env python3

import numpy as np

procedure = ['P1','P2','P3','P5','Unit sterilisasi','P9','P11','Unit Pasteurisasi','P15',
             'P16','P18','P19','P20','P22','P23']
nama = ['lyon','dhea','kel']

procedure = np.random.permutation(procedure)
nama = np.random.permutation(nama)

print('{} : {}'.format(nama[0],procedure[:5]))
print('{} : {}'.format(nama[1],procedure[5:10]))
print('{} : {}'.format(nama[2],procedure[10:]))
