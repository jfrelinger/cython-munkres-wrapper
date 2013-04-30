# Import the Python-level symbols of numpy
import numpy as np

# Import the C-level symbols of numpy
cimport numpy as np

cimport cython # to disable bounds checks
# Numpy must be initialized. When using numpy from C or Cython you must
# _always_ do that, or you will have segfaults
np.import_array()



cdef extern from "cpp/Munkres.h":
    cdef cppclass Munkres:
        Munkres()
        void solve(double* icost, int* answer, int m, int n)

@cython.boundscheck(False)
def munkres(np.ndarray[np.double_t,ndim=2, mode="c"] A not None):
    '''
    calculate the minimum cost assigment of a cost matrix (must be numpy.double type)
    '''
    cdef int x = A.shape[0]
    cdef int y = A.shape[1]
    
    cdef np.ndarray rslt
    rslt = np.zeros(shape=(x,y), dtype=np.int32, order='c')
    cdef Munkres* munk = new Munkres()
    munk.solve(<double *> A.data, <int *> rslt.data, x, y)
    del munk
    return rslt.astype(np.bool)

@cython.boundscheck(False)
def max_cost_munkres(np.ndarray[np.double_t,ndim=2] A not None, double max_cost):
    cdef int x = A.shape[0]
    cdef int y = A.shape[1]
    
    cdef np.ndarray[np.double_t, ndim=2, mode="c"] B = np.empty(shape=(x, y+x), dtype=np.double, order='c')
    B[:,0:y] = A
    B[:,y:] = max_cost
    return munkres(B)[:,0:y]

@cython.boundscheck(False)
def iterative_munkres(icost, max_cost):
    cost = icost.copy()
    dim = np.arange(cost.shape[1])
    done = False
    assigned = np.zeros(shape=cost.shape, dtype=np.bool)
    while not done:
        r = max_cost_munkres(cost, max_cost)
        for i,j in enumerate(r):
            if np.any(j):
                assigned[i, dim[j]] = True
                cost[i,dim[j]] = max_cost+1
        if not np.any(r):
            done = True
    return assigned