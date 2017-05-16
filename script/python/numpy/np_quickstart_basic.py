import numpy as np
from numpy import pi
a = np.arange(15).reshape(3,5)
print a
print a.shape
print a.ndim
print a.dtype.name
print a.itemsize
print a.size
print type(a)

print "********"

t1 = (1,2,3)
t2 = (4,5,6)
t3 = (7,8,1000)
c = [6,7,8]
d = [t1,t2, t3]
# b = np.array([6,7,8])
b = np.array(d)
print b
print b.shape
print b.ndim
print b.dtype.name
print b.itemsize
print b.size
print type(b)

print "********"

# e = np.array( [ [1,2], [3,4] ], dtype=complex )

e = np.array( [ [1,2], [3,4] ], dtype=complex )

print e

print "******f"
f = np.zeros( (3,4) )
print f

print "******g"
g = np.ones( (2,3,4), dtype=np.int16 )
print g
print g.shape
print g.ndim

print "******h"
h = np.empty( (2,3) )
print h

print "*******i"
i = np.arange( 10, 30, 5 )
print i

print "*******j"
j = np.arange( 0, 2, 0.3 )
print j

print "*******k"
k = np.linspace( 0, 1.8, 7 )
print k


print "*******l"
l = np.linspace( 0, 2*pi, 100 )
# print l
print 10 * np.sin(l)

print "*******a1"
a1 = np.arange(6)
print a1

print "*******a2"
a2 = np.arange(12).reshape(4,3)
print a2

print "*******a3"
a3 = np.arange(24).reshape(2,3,4)
print a3

print "*******a4"
a4 = np.arange(10000)
print a4

print "*******a5"
a5 = np.arange(10000).reshape(100,100)
print a5

print "*******a6 a7 a8"
a6 = np.array( [20,30,40,50] )
a7 = np.arange( 4 )
a8 = a6 - a7
print a8
print a7**2
print 10 * np.sin(a6)
print a6 < 35

print "*******a9 a10 a11"
a9 = np.array( [[1,1],[0,1]] )
a10 = np.array( [[2,0],[3,4]] )
print a9 * a10
print a9.dot(a10)
print np.dot(a9, a10)

print "*******a12 a13"
a12 = np.ones((2,3), dtype=int)
a13 = np.random.random((2,3))
print 5*np.random.random_sample((3, 2)) - 5
print a12
a12 *= 3
print a12
print a13
a13 += a12
print a13

print "*******a14 a15 a16 a17"
a14 = np.ones(3, dtype=np.int32)
a15 = np.linspace(0,pi,3)
print a14,a15
print a15.dtype.name
a16 = a14 + a15
print a16
print a16.dtype.name
a17 = np.exp(a16*1j)
# print a16*1j
print a17,a17.dtype.name


print "*******a18 "
a18 = np.random.random((2,3))
print a18,a18.sum(),a18.max(),a18.min()

print "*******a19 "
a19 = np.arange(12).reshape(3,4)
print a19,a19.sum(axis=0),a19.min(axis=1), a19.max(axis=1)
print a19.cumsum(axis=0)
print "----"
print np.cumsum(a19),np.min(a19, axis=1), np.max(a19, axis=0)
