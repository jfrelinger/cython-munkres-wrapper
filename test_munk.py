import numpy as np
import munkres

a = np.array([i for i in range(64)], dtype=np.double).reshape((8,8))
print munkres.munkres(a)
a = np.array(map(float,'7 4 3 6 8 5 9 4 4'.split()), dtype=np.double).reshape((3,3))
b = munkres.munkres(a)
print b
print a[b]