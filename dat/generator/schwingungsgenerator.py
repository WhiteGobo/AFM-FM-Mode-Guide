#!/usr/bin/env python
import numpy as np

def makesafefile(xarray, yarray, name="test.dat"):
    savearray = np.array([xarray, yarray]).T
    np.savetxt(dest + name, savearray)

def makesafefile_cond1(xarray, yarray, name="test.dat"):
    mask_array = np.zeros(yarray.shape)
    for n in range(mask_array.size):
        if yarray[n] > 10:
            mask_array[n]=1
    xarray = np.ma.masked_array(xarray,mask=mask_array)
    yarray = np.ma.masked_array(yarray,mask=mask_array)
    savearray = np.array([xarray.compressed(), yarray.compressed()]).T
    np.savetxt(dest + name, savearray)

pi=3.141592653

dest = "../"

xarray = np.linspace(0.6,3,120)

Amplitude = [1, 1]
Radius = [1, 1.2]
for n in range(0,2):
    yarray = Amplitude[n] * ((Radius[n]/xarray)**12 - 2*(Radius[n]/xarray)**6)
    makesafefile_cond1(xarray, yarray, name="lennard" + str(n) + ".dat")


