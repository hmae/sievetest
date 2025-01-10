#! env\Scripts\python.exe
# -*- coding: utf-8 -*-

"""
Created on Mon Aug 02 18:34:31 2021

@author: hmae
"""
import pandas
import numpy as np
from shapely.geometry import LineString
from matplotlib import pyplot as plt

fn = 'Book1.xlsx'
df = pandas.read_excel(fn)

dfarray = df.dropna()
print(dfarray)
dfarray = dfarray.to_numpy()
print(dfarray)
xs = dfarray[:-1,0]
ret = dfarray[:-1,1]
ys = dfarray[:-1,4]

line1 = LineString(np.column_stack((xs, ys)))
P10 = LineString(np.column_stack((xs,np.ones_like(xs)*10)))
P30 = LineString(np.column_stack((xs,np.ones_like(xs)*30)))
P60 = LineString(np.column_stack((xs,np.ones_like(xs)*60)))


fig, ax = plt.subplots(1,1)
ax.set_ylim(-5,105)
ax.semilogx()
ax.set_xlim(0.02, max(xs)+5)
ax.set_title("Grain Size Distribution Curve")
ax.set_xlabel("Sieve Size mm")
ax.set_ylabel("Percentage of Fine Materials %")
ax.grid(True, which='both')

nx ,ny = [],[]
for i, r in enumerate(ret):
    if r != 0:
        nx.append(xs[i])
        ny.append(ys[i])
print(nx, ny, sep='\n')

ax.plot(nx, ny, c='purple', alpha=0.5)

intersections = []
for p in [P10, P30, P60]:
    if line1.crosses(p):
        p = line1.intersection(p)
        intersections.append(p.x)
        ax.scatter(*p.xy, marker='+', s=100, label=f"{round(p.x,4)} - D{int(p.y)}")
    else:
        intersections.append(False)
    
results = pandas.DataFrame(intersections, index=['D10','D30','D60'])
print('-------------')
print(results)
print('-------------')

plt.legend()
plt.show()


