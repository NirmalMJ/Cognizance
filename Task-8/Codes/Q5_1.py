import numpy as np
  
array1 = np.array([[5, 23, 51], [513, -52, 70],[-52, 72, 221]])
array2 = np.array([[12, -34, 61], [12, 134, 14],[23, 4, 23]])
   
print ("Array 1 : \n", array1) 
print ("Array 2 : \n", array2) 
    
added = np.add(array1, array2) 
print ("\nArray 1 + Array 2 = \n", added)