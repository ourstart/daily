import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.interpolate
import pandas as pd

# scikit
import sklearn
import sklearn.ensemble
import sklearn.metrics
import sklearn.utils
import sklearn.cross_validation
import sklearn.isotonic

plt.ion()
# Simulate some true and observed data
offset = 33
slope1 = 10
slope2 = 2
points = 1000
x = np.linspace(0, 100, points)
y_true = 100 - ((x < offset) * x * slope1 + (x >= offset) * ((x-offset) * slope2 + (offset * slope1)))
y_observed = y_true + (0.5 - np.random.random(y_true.shape)) * np.sin(100-x) * (100-x) * 2

#matplotlib inline
plt.figure(figsize=(10, 8))
plt.title('Isotonic Example')
plt.xlabel('x')
plt.ylabel('y')
plt.scatter(x, y_true, alpha=0.5, color='blue')
plt.scatter(x, y_observed, alpha=0.5, color='red')
plt.legend(('True', 'Observed'))
plt.show()
