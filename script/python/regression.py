import pandas as pd
import matplotlib.pyplot as plt

x = [[150.0], [200.0], [250.0], [300.0], [350.0], [400.0], [600.0]]
y = [6450.0, 7450.0, 8450.0, 9450.0, 11450.0, 15450.0, 18450.0]
plt.scatter(x,y,color='blue')


plt.plot(x,y,linestyle='--',color='green')
plt.plot()
plt.xticks()
plt.yticks()
plt.show()
