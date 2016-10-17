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

def fourrier(xarray,yarray, k):
    if xarray.size != yarray.size:
        return 0
    a=0
    b=0
    for n in range(yarray.size):
        a += yarray[n]*np.sin(k * xarray[n])
        b += yarray[n]*np.cos(k * xarray[n])
    b -= (yarray[0] + yarray[yarray.size-1]) /2
    a *= xarray[1] - xarray[0]
    b *= xarray[1] - xarray[0]
    return a,b

def mittel_settozero(array):
    tmp = 0
    for x in array:
        tmp += x

    tmp /= array.size
    back = array - tmp
    return back


pi=3.141592653

dest = "../"

xarray = np.linspace(0.6,10,420)

Amplitude = [1, 1, 3, 0]
Radius = [1, 1.2, 2,2]
for n in range(0,2):
    yarray = Amplitude[n] * ((Radius[n]/xarray)**12 - 2*(Radius[n]/xarray)**6)
    makesafefile_cond1(xarray, yarray, name="lennard" + str(n) + ".dat")

for n in range(2,4):
    yarray = Amplitude[n] * ((Radius[n]/xarray)**12 - 2*(Radius[n]/xarray)**6) -0.5*xarray
    makesafefile_cond1(xarray, yarray, name="lennardetfeder" + str(n) + ".dat")


for n in range(2,4):
    tarray = np.linspace(0,2*np.pi,100)
    xtarray = 5 + 2*np.sin(tarray)
    ytarray = Amplitude[n] * ((Radius[n]/xtarray)**12 - 2*(Radius[n]/xtarray)**6) -0.5*xtarray
    makesafefile(tarray, ytarray, name="lennardetfedertime" + str(n) + ".dat")
    makesafefile(tarray, xtarray, name="lennardetfedertime_osci" + str(n) + ".dat")
    ytarray = mittel_settozero(ytarray)
    ytarray_sin = np.zeros(tarray.shape)
    ytarray_cos = np.zeros(tarray.shape)
    for k in range(10):
        tmp1, tmp2 = fourrier(tarray, ytarray, k)
        ytarray_sin += tmp1* np.sin(k*tarray)
        ytarray_cos += tmp2* np.cos(k*tarray)
    makesafefile(tarray, ytarray_sin, name="lennardetfedertime_sin" + str(n) + ".dat")
    makesafefile(tarray, ytarray_cos, name="lennardetfedertime_cos" + str(n) + ".dat")
     
