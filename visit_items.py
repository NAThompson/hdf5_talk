#!/usr/bin/env python3

import h5py

def print_attrs(name, obj):
    print(name)
    l = list(obj.attrs)
    if len(l) > 0:
        print(list(obj.attrs))

f = h5py.File('stocks.hdf5', 'r')
f.visititems(print_attrs)
