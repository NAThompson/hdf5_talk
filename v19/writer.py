#!/usr/bin/env python3

import h5py
import numpy as np
import time
from multiprocessing import Process, Event

f = h5py.File('growing.h5', 'w', libver='latest')
arr = np.array([1,2,3,4])

dset = f.create_dataset('/vector', chunks=(2,), maxshape=(None, ), data=arr, fillvalue=12)
f.swmr_mode = True


while True:
    new_shape = (2*len(arr), )
    arr = np.ones(shape=new_shape)
    dset.resize(new_shape)
    print("Writing data:")
    dset[...] = arr
    dset.flush()
    time.sleep(5)
