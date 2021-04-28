import numpy as np
import matplotlib.pyplot as plt


datas = np.genfromtxt("final_data.csv", delimiter=',')


plt.plot([0, -10, -20, -30, -40 ,-50, -60],datas[0] ,'r',label='0.5Ghz')
plt.plot([0, -10, -20, -30, -40 ,-50, -60],datas[1] ,'b',label='1Ghz')
plt.plot([0, -10, -20, -30, -40 ,-50, -60],datas[2] ,'g',label='2Ghz')
plt.plot([0, -10, -20, -30, -40 ,-50, -60],datas[3] ,'k',label='3Ghz')
plt.plot([0, -10, -20, -30, -40 ,-50, -60],datas[4] ,'y',label='4Ghz')
plt.xlabel('Input Power (dBm)')
plt.ylabel('ADC Code')
plt.title('CN0150 Test')
plt.legend()
plt.grid()
plt.show()

