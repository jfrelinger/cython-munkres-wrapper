import numpy as np
from munkres import munkres

a = np.array([i for i in range(64)], dtype=np.double).reshape((8,8))
print munkres(a)
a = np.array(map(float,'7 4 3 6 8 5 9 4 4'.split()), dtype=np.double).reshape((3,3))
print munkres(a)

a = np.array(map(float,'7 4 3 6 8 5 9 4 4 3 3 3'.split()), dtype=np.double).reshape((4,3))
print munkres(a)

#a = np.array(map(float,'7 4 3 3 6 8 5 3 9 4 4 3'.split()), dtype=np.double).reshape((3,4))
#print munkres(a)