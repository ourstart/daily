import numpy as np
from numpy import pi

print "*******a1 a2*** np.arange(), np.exp(), np.sqrt() np.add()"
a1 = np.arange(3)
print a1
print np.exp(a1)
print np.sqrt(a1)
a2 = np.array([2., -1., 4.])
print np.add(a1,a2)


print "*******a3 a4"
a3 = np.array([1,2,3])
a4 = np.array([1,5,7])
print np.corrcoef(a3, a4)
a4 = [1,2,3]
a5 = [1,5,7]
print np.cov(a4, a5)
