import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state

n = 16
# x = np.arange(n)
#
# rs = check_random_state(0)
# y = rs.randint(-50, 50, size=(n,)) + 50. * np.log(1 + np.arange(n))
x = [2.25,2.25,2.25,3.6,5.45,5.5,5.55,5.5,6.2,6.4,6.35,6.4,6.5,6.4,6.35,6.45]
y = [199.1,201.88,199.67,410.42,774.28,775.97,776.53,775.95,903.6,936.92,942.45,940.45,938.1,940.59,944.06,943.58]



###############################################################################
# Fit IsotonicRegression and LinearRegression models

ir = IsotonicRegression()

y_ = ir.fit_transform(x, y)

pp = ir.predict([50, 60])
print pp

# lr = LinearRegression()
# lr.fit(x[:, np.newaxis], y)  # x needs to be 2d for LinearRegression

###############################################################################
# plot result

segments = [[[i, y[i]], [i, y_[i]]] for i in range(n)]
lc = LineCollection(segments, zorder=0)
lc.set_array(np.ones(len(y)))
lc.set_linewidths(0.5 * np.ones(n))

fig = plt.figure()
plt.plot(x, y, 'r.', markersize=12)
plt.plot(x, y_, 'g.-', markersize=12)
# plt.plot(x, lr.predict(x[:, np.newaxis]), 'b-')
plt.gca().add_collection(lc)
plt.legend(('Data', 'Isotonic Fit', 'Linear Fit'), loc='lower right')
plt.title('Isotonic regression')
plt.show()
