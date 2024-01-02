import numpy as np

lst = [1, 2, 3, 4, 5]

#partially initialized module 'numpy' has no attribute 'array' (most likely due to a circular import) 
#solution == change project name form numpy.py to something else

numpy_from_list1 = np.array(lst)
print(type(numpy_from_list1))

numpy_from_list2 = np.array(lst, dtype= float)
print(numpy_from_list2)