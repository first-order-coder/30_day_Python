import numpy as np

lst = [1, 2, 3, 4, 5]

#partially initialized module 'numpy' has no attribute 'array' (most likely due to a circular import) 
#solution == change project name form numpy.py to something else

# numpy_from_list1 = np.array(lst)
# print(type(numpy_from_list1))

# numpy_from_list2 = np.array(lst, dtype= float)
# print(numpy_from_list2)

a = np.array([1, 3 ,5])
b = np.array([3, 5, 7])

c = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8]]) #2 dimensional array

print(c.ndim) #which dimension 2
print(c.shape) #the shape (2,4)

print(c.itemsize) #4 bytes (data value size)
print(c.size) #how many elements

''' In numpy rows and columns indexes start from 0 but in Matlab index starts from 1'''
print(c[1,2]) #answer 7 

print(c[0,:]) #get the whole first row (0 th index)

d = np.array([[[1,2],
               [2,3]],

              [[5,6],
               [7,8]]]) #3d array
print(d)
print(d.size) #number of elements
print(d.ndim)
print(d.min()) #minimum value
print(d.max()) #maximum value

print(d[1,0,0]) #5

print(np.zeros((3,3,3))) #3d matrix with all zeroes

print(np.ones((4,2))) #matrix with all ones

print(np.random.rand(4,2)) #random decimal numbers
print(np.random.randint(2,7, size=(5,5))) #randint(low, high, size=(rows,columns))
print(np.random.random((5,5))) #random float numbers

''' To get the determinant of a Square Matrix '''
e = np.random.randint(1,10, size=(3,3))
print('\n',e)

determinant = np.linalg.det(e)
print(determinant)

print(np.linspace(1, 5, num=6))
print(np.linspace(1, 5, num=6, endpoint=False)) #if we dont want to include 5(the end number)

print(np.identity(3))

''' array filled with 0s except for nth diagonal '''
z = np.eye(3,k=0) #array([[1., 0., 0.],
                       #  [0., 1., 0.],
                       #  [0., 0., 1.]])
            
''' Each elemnt by element will be divided and remainder will be outputted in Matrix '''

f = np.random.randint(2, 10, size=(3,3))
g = np.random.randint(2, 15, size=(3,3))
print('\n',f)
print('\n',g)

divised = np.mod(f, g)
print(divised)

print(f.flatten()) #any dimension matrix will be converted to 1D array
