import numpy as np
from munkres import munkres

def test_simple():
    a = np.array([i for i in range(64)], dtype=np.double).reshape((8, 8))
    b = munkres(a)
    truth = np.zeros((8, 8), dtype=np.bool)
    for i in range(8):
        truth[7 - i, i] = True
    np.testing.assert_array_equal(b, truth, 'simple 8x8 case failed, b=%s, truth=%s' % (str(b), str(truth)))

def test_basic():
    a = np.array(map(float, '7 4 3 6 8 5 9 4 4'.split()), dtype=np.double).reshape((3, 3))
    b = munkres(a)
    truth = np.array([[False, False, True],
                      [ True, False, False],
                      [False, True, False]])
    np.testing.assert_array_equal(b, truth, 'basic 3x3 case failed, a=%s, truth=%s' % (str(a), str(truth)))

def test_more_candidates():

    a = np.array(map(float, '7 4 3 6 8 5 9 4 4 10 10 10'.split()), dtype=np.double).reshape((4, 3))
    b = munkres(a)
    truth = np.array([[False, False, True],
                      [True, False, False],
                      [False, True, False],
                      [False, False, False]])
    
    np.testing.assert_array_equal(b, truth, 
                                  'basic 4x3 case failed\na=%s\ntruth=%s\ncost=%s\ntrue_cost=%s' % (str(a), str(truth), str(a[b]), str(a[truth])))
    

def test_more_jobs():
    a = np.array(map(float, '7 4 3 3 6 8 5 3 9 4 4 3'.split()), dtype=np.double).reshape((3, 4))
    b = munkres(a)

    truth = np.array([[False, False, True, False],
                      [False, False, False, True],
                      [False, True, False, False]])
    np.testing.assert_array_equal(b, truth, 
                                  'basic 3x4 case failed\na=%s\ntruth=%s\ncost=%s\ntrue_cost=%s' % (str(a), str(truth), str(a[b]), str(a[truth])))
                  

def test_big():
    a = np.empty((256,256))
    for i in range(256):
        for j in range(256):
            a[i,j] = (i+1)*(j+1)
    b = munkres(a.T)
    print b
