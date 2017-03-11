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




# xMat = mat(xArr)
# srtInd = xMat[:,1].argsort(0)
# xSort = xMat[srtInd][:, 0, :]
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(xSort[:, 1], yHat[srtInd])
# ax.scatter(xMat[:, 1].flatten().A[0], mat(yArr).T.flatten().A[0], s = 2, c = "red")
# plt.show()


# xArr,yArr = loadDataSet('/Users/ourstart/github/daily/script/python/ch08/ex0.txt')
# print xArr[0:2]
# ws = standRegres(xArr, yArr)
# print ws
# xMat = mat(xArr)
# yMat = mat(yArr)
# yHat = xMat * ws
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0])
# xCopy = xMat.copy()
# xCopy.sort(0)
# yHat = xCopy*ws
# ax.plot(xCopy[:, 1], yHat)
# plt.show()
