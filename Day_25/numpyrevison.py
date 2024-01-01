import numpy as np

a = np.array([1, 2, 3])
# print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])
# print(b)

c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8 ,9], [10, 11, 12]]])
# print(c.ndim)
# print(c[0, 1, 0])
# print(c[1, 0, :])
# print(b.size)
# print(b.itemsize)

''' All zeroes array, have to use paranthesis cause other wise second nnumber is taken as data type'''
a1 = np.zeros((5, 5), int)
# print(a1)
''' All ones array '''
a2 = np.ones((3, 3), int)
# print(a2)
''' Any other number'''
a3 = np.full((2, 2, 2), 99)
# print(a3)
a4 = np.random.rand(4, 4)
# print(a4)
b1 = np.random.randint(7, size= (5, 5))
# print(b1)
b2 = np.random.randint(5, size=(3,3)) #from 0 to 5 and 5 exculuded
# print(b2)
b3 = np.random.randint(3, 9, size=(3,4))
# print(b3)
c1 = np.identity(3, int) #identity matrix
# print(c1)

'''In 2 and 3 dimensional arrays y axis = 0 nad x axis = 1'''

''' Changing the value of an elemnt of an array'''
c1[1,1] = 9
# print(c1)

''' To copy an array correctly'''

c2 = np.array([1, 2, 3])
b12 = c2.copy()
b12[1] = 5
# print(b12) 
# print(c2)

''' +, -, /, * are same on numpy arrays'''
c2 = np.ones((4, 4), int)
# print(c2 ** 2)

x = np.cos(c2)
# print(x)

# z = np.full((size), value)
''' Multiplying two arrays'''
z = np.full((4,4), 5)
y = np.random.randint(5, size=(3,3))
# print(np.dot(y,z))

''' Finding the determinant of a matrix, matrix must be and square matrix'''
# print(np.linalg.det(y))

''' Identity matrix diagonals = 1 while all others = 0'''
z1 = np.identity(3, int)
# print(z1)

''' Re shaping arrays '''
before = np.array([[1, 2, 6], [3, 4, 5]])
# print(before)
after = before.reshape((6, 1)) #before and after reshaping sizes have to be same 
# print(after)

''' Horizontal stacking and Vertical Stacking '''
h1 = np.array([2,4])
h2 = np.array([2,3])
# print(np.vstack([h1, h2]))
# print(np.hstack([h1, h2]))

# n = np.random.randint(5, size=(4,3))
q = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [8, 9, 10, 11], [12, 13, 14, 15]])
# print(q[[0,1,2,3], [0,1,2,3]]) #[ 1 6 10 15]
# print(q[[0, 1, 2], [1, 2, 3]]) #[ 2 7 11]
# print(q[0, 1:])
