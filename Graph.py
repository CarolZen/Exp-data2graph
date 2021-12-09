# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_table("D:/inca/S03BB423.txt")

#Set X，Y
x_data=np.array(data['PI-01'][3:10])
y_data=np.array(data['AI-01'][3:10])
x_data=x_data.astype('float64')
y_data=y_data.astype('float64')

plt.title("FullLoad")
plt.xlabel("NE(rpm)")
plt.ylabel("torque(Nm)")
plt.xlim((800,2400))
plt.ylim((0,300))

l1=plt.plot(x_data, y_data,color='red',linestyle='solid',marker='o',ms=5)
plt.legend(['sample'])
plt.grid()  #plt.grid(axis='x')
plt.text(1800, 220, 'target',color='b')
plt.show()