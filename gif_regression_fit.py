#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 19:33:48 2023

@author: quentin
test
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
!pip install seaborn
import seaborn as sns
from toolstat import colors
import math

df=pd.read_excel('/Users/quentin/Downloads/fake_data_mmm.xlsx')

X=np.linspace(1000, 3000)
c = 6000

def f(slope, c=6000):
    return X * slope + c

def findm(y0,y):
    if y0<y:
        return y0, y
    else:
        return y, y0
k=1
slopes=[4, 3, 1.9, 1.1, 0.8, 2.3, 2.2, 0.9, 1.4, 1.5, 1.6, 3.5, 1.8, 1.9, 2, 3.1, 3.4,1.2, 1.1, 3.7, 0.8, 0.6, 3.8, 2]    
errors=[]
all_slopes=[]
for slope in slopes:    
    y=f(slope)
        
    plt.style.use('ggplot')
    fig, (ax,ax1)=plt.subplots(1, 2, figsize=(9,5))
    ax.scatter(df['Daily spend on TT'], df['Daily sales'], color=colors[1])
    ax.set_xlabel('Daily TT Spend')
    ax.set_ylabel('Daily sales')
    ax.plot(X, y, color=colors[0])
    
    # pick points and compute errors
    summ=0
    for i in range(40):
        x0=df.iloc[i]['Daily spend on TT']
        y0=df.iloc[i]['Daily sales']
        
        y1=slope*x0+c
        ymin, ymax=findm(y0,y1)
        ax.vlines(x=x0, ymin=ymin, ymax=ymax, color='black', linestyle='dashed', alpha=0.7)
    
        summ+=ymax-ymin
    errors.append(summ.sum())
    all_slopes.append(slope)
    # Print errors
    ax.text(x=1500, y=13000, s=f'Error: {math.floor(summ)}', color='black', fontsize=15)
    ax1.scatter(all_slopes, errors)
    ax1.set_title('Errors by slope')
    plt.savefig(f'{k}.png', transparent=True)
    k+=1
    plt.show()