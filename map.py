# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 04:02:57 2016

@author: 伸太郎
"""

# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure(figsize=(10,10))
m = Basemap(projection='merc',llcrnrlat=25.0,urcrnrlat=50.0,\
            llcrnrlon=125.0,urcrnrlon=150.0,resolution='i')
m.drawcoastlines(linewidth=0.5, color='black')
m.fillcontinents(color='#ffffbf',lake_color='white')
#m.drawstates( linewidth=0.5, color='#000000' )
#m.drawcountries(linewidth=0.5, color='#000000')
m.drawmapboundary(fill_color='skyblue')

m.drawparallels(np.arange(25,50,5), labels = [1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(125,150,5), labels = [0,0,0,1], fontsize=10)
fnameF = "fig_japan.png"
plt.savefig(fnameF)
plt.show()
