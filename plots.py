# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:29:02 2017

@author: behzad
"""
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
#import seaborn as sns
sns.set(style="whitegrid", color_codes=True)

time1 = [0.024, 0.010, 0.030, 0.004, 0.029, 0.024, 2.34]
time2 = [11.197, 2.885, 39.027, 6.245, 38.733, 11.286, 262.783]
time3 = [83.182, 1.459, 372.161, 94.131, 350.436, 73.722, 1821.1]

expan1 = [43, 21, 55, 7, 55, 41, 11]
expan2 = [3343, 624, 4853, 998, 4853, 1506, 86]
expan3 = [14663, 408, 18223, 5578, 18223, 5118, 408]
goal1 = [56, 22, 57, 9, 57, 43, 13]
goal2 = [4609, 625, 4855, 1000, 4855, 1508, 88]
goal3 = [18096, 409, 18225, 5580, 18225, 5120, 410]
new1 = [180, 84, 224, 28, 224, 170, 50]
new2 = [30509, 5602, 44041, 8982, 44041, 13820, 841]
new3 = [129631, 3364, 159618, 49150, 159618, 45650, 3758]




N = 7
ind = np.arange(N)  # the x locations for the groups
width = 0.25      # the width of the bars

fig, ax = plt.subplots()
#time = ax.bar(ind, time2, width, color='r')
expansions = ax.bar(ind, expan3, width, color='b')
goal_test = ax.bar(ind + width, goal3, width, color='r')
new_nodes = ax.bar(ind + 2 * width, new3, width, color='g')

# add some text for labels, title and axes ticks
ax.set_ylabel('Number')
ax.set_title('Air Cargo Problem 3')
#ax.set_xticks(ind + 2 * width / 2)
ax.set_xticks(ind + 2 * width / 3)
ax.set_xticklabels(('BFS', 'DFS Graph', 'UCS', 'Greedy H1', 'A* H1', 'A* Ignore', 'A* Levelsum'))

#ax.legend((expansions, goal_test, new_nodes), ('Expansions', 'Goal Test', 'New Nodes'))

#plt.show()

#autolabel(rects2)

plt.show()
