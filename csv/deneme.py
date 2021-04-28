import numpy as np
import os


raw_data = np.genfromtxt("data_edit.csv", delimiter=',')

f = open("final_data.csv", 'w')

for x in range(len(raw_data)):
    try:
        data=raw_data.T[x]
        f.write("{}\n".format(data))
    except IndexError:
        pass
