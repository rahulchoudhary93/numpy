"""
Let us learn some Numpy...
Numpy is an open-source library used to implement arrays in Python.
It provides several features to ease data manipulation
"""
#We import Numpy
import numpy as np

"""Let us create the simplest Numpy Array with a Python List. We can also use tuples."""
python_list = [2, 7, 8, 9, 7]
numpy_array = np.array(python_list)
print(numpy_array)
"""O/P - [2 7 8 9 7]"""

"""Numpy provides an interesting arange function to create a array of integers where the end value is exclusive.
Documentation : https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.arange.html"""
nprange = np.arange(4, 19, 3)
print(nprange)
"""O/P - [ 4  7 10 13 16]"""

"""Numpy linspace() method provides an array with linear spacing between the start and end points inclusive.
Documentaion : https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html"""
nplinspacearray, spacing = np.linspace(3, 9, 6, endpoint=True, retstep=True, dtype=float)
print(nplinspacearray, spacing)
"""O/P - [3.  4.2 5.4 6.6 7.8 9. ] 1.2"""

"""Numpy zeros() initializes an array with all the element values as zero"""
zeroarray = np.zeros(5, dtype=int)
print(zeroarray)
"""O/P - [0 0 0 0 0]"""
zeroarray[-1] = 9
print(zeroarray)
"""O/P - [0 0 0 0 9]"""

"""Numpy ones() initializes an array with all the element values as one"""
onesarray = np.ones((3,2,4)) #Notice that by default we have dtype=float
print(onesarray)
"""O/P - 
 [[[1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]]]"""
print(len(onesarray))
"""O/P- 3"""
print(onesarray.size)
"""O/P - 24"""
print(onesarray.ndim)
"""O/P - 3"""
print(onesarray.shape)
"""O/P - (3, 2, 4)"""
print(onesarray.dtype)
"""O/P - float64"""
print(type(onesarray))
"""O/P - <class 'numpy.ndarray'>"""
onesarray[1, 0, 3] = 9
print(onesarray)
"""O/P - 
[[[1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[1. 1. 1. 9.]
  [1. 1. 1. 1.]]

 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]]]"""

"""Masking"""
np1 = np.array([2, 4, 3, 61, 8])
np2 = np.array([True, False, True, True, False])
np3 = np1[np2]
np4 = 0 == np1 % 2
print(np3)
print(np4)
print(np.logical_and(np2, np4))
"""O/P- 
[ 2  3 61]
[ True  True False False  True]
[ True False False False False]
"""

"""Broadcasting"""
np5 = np.arange(0, 60).reshape(4, 3, 5)
print(np5)
print("-----sum()-----")
print(np5.sum())
print("-----sum(0)-----")
print(np5.sum(0))
print("-----sum(1)-----")
print(np5.sum(1))
print("-----sum(2)-----")
print(np5.sum(2))
np6 = np5 // 2 +2
print("-----np6-----")
print(np6)
"""O/P - 
[[[ 0  1  2  3  4]
  [ 5  6  7  8  9]
  [10 11 12 13 14]]

 [[15 16 17 18 19]
  [20 21 22 23 24]
  [25 26 27 28 29]]

 [[30 31 32 33 34]
  [35 36 37 38 39]
  [40 41 42 43 44]]

 [[45 46 47 48 49]
  [50 51 52 53 54]
  [55 56 57 58 59]]]
-----sum()-----
1770
-----sum(0)-----
[[ 90  94  98 102 106]
 [110 114 118 122 126]
 [130 134 138 142 146]]
-----sum(1)-----
[[ 15  18  21  24  27]
 [ 60  63  66  69  72]
 [105 108 111 114 117]
 [150 153 156 159 162]]
-----sum(2)-----
[[ 10  35  60]
 [ 85 110 135]
 [160 185 210]
 [235 260 285]]
-----np6-----
[[[ 2  2  3  3  4]
  [ 4  5  5  6  6]
  [ 7  7  8  8  9]]

 [[ 9 10 10 11 11]
  [12 12 13 13 14]
  [14 15 15 16 16]]

 [[17 17 18 18 19]
  [19 20 20 21 21]
  [22 22 23 23 24]]

 [[24 25 25 26 26]
  [27 27 28 28 29]
  [29 30 30 31 31]]]
"""

"""Structured Arrays"""
student_data_type = [('Name', 'S8'), ('ID', 'i8'), ('class', 'i8')]
student_data = np.zeros((3, 2, 3), dtype=student_data_type)
print(student_data, student_data.dtype)
"""O/P-
[[[(b'', 0, 0) (b'', 0, 0) (b'', 0, 0)]
  [(b'', 0, 0) (b'', 0, 0) (b'', 0, 0)]]

 [[(b'', 0, 0) (b'', 0, 0) (b'', 0, 0)]
  [(b'', 0, 0) (b'', 0, 0) (b'', 0, 0)]]

 [[(b'', 0, 0) (b'', 0, 0) (b'', 0, 0)]
  [(b'', 0, 0) (b'', 0, 0) (b'', 0, 0)]]]
  
  [('Name', 'S8'), ('ID', '<i8'), ('class', '<i8')]
"""
student_data[1, 0, 2] = ('John', 1212, 3)
print(student_data)
"""O/P-
[[[(b'',    0, 0) (b'',    0, 0) (b'',    0, 0)]
  [(b'',    0, 0) (b'',    0, 0) (b'',    0, 0)]]

 [[(b'',    0, 0) (b'',    0, 0) (b'John', 1212, 3)]
  [(b'',    0, 0) (b'',    0, 0) (b'',    0, 0)]]

 [[(b'',    0, 0) (b'',    0, 0) (b'',    0, 0)]
  [(b'',    0, 0) (b'',    0, 0) (b'',    0, 0)]]]
"""

print(student_data['ID'][1,0,2])
"""O/P- 1212"""

"""Record Arrays"""
rec_numpy_array = np.rec.array([('John', 21, 2), ('Jack', 22, 3)], dtype=student_data_type)
print(rec_numpy_array[0].ID)
"""O/P - 21"""






