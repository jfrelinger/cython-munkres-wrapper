Munkres Readme
==============

Munkres calculates the minimum cost assignment of the assignment
using the Hungarian/Munkres algorithm.

Usage
=====
::

  from munkres import munkres
  import numpy as np
  a = np.array(map(float,'7 4 3 6 8 5 9 4 4'.split()), dtype=np.double).reshape((3,3))
  print munkres(a)

which should print out ::

 [[False False  True]
  [ True False False]
  [False  True False]]
