#!/usr/bin/env python3

import h5py
import numpy as np
import time

f = h5py.File('growing.h5', 'r', libver='latest', swmr=True)
dset = f['/vector']

while True:
    print("Refreshing dataset")
    dset.refresh()
    shape = dset.shape
    print("Shape of dset: {}".format(str(shape)))
    time.sleep(5)
